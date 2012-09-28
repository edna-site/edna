# coding: utf8
#
#    Project: The EDNA Kernel
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2008-2012 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal authors: Marie-Francoise Incardona (incardon@esrf.fr)
#                       Olof Svensson (svensson@esrf.fr) 
#                       Jérôme Kieffer (jerome.kieffer@esrf.eu)
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
__doc__ = """
The purpose of this plugin execute class is to be subclassed for
creating plugins that execute external programs through scripts.
"""
import os, shlex, sys
from EDVerbose              import EDVerbose
from EDUtilsFile            import EDUtilsFile
from EDUtilsPath            import EDUtilsPath
from EDPluginExecProcess    import EDPluginExecProcess
from EDConfiguration        import EDConfiguration
from EDUtilsPlatform        import EDUtilsPlatform
from XSDataCommon           import XSPluginItem


class EDPluginExecProcessScript(EDPluginExecProcess):
    """
    The super class for all EDNA plugins that execute a task using a script.
    This class manages the process script to be executed:
        - Configuration options:
              - execProcessScriptShell         : The shell that will execute the script, written into the top line of the script, for example : #!/bin/bash
              - execProcessScriptExecutor      : If defined, this command is used for launching the shell. 
              It can be used for example to launch the shell using a grid engine. (Note that the example to launch the shell using a grid engine. 
              (Note that the execProcessScriptExecutor will be replaced by execProcessExecutable)
              - execProcessScriptExecutable    : The path to the third-party executable that will be launched in the script.
              - execProcessScriptSetupCCP4     : Path to CCP4 setup file (if required)
              - execProcessScriptVersionString : A string which describes the version of the execProcessScriptExecutable, 
              which should match the version string written into the program log, for example: "Version 7.0.1  for Image plate and CCD data 20th August 2007"
              (Note that this configuration option will be moved to EDPluginExecProcess)
        - The list of compatible 3rd party executable version the plugin should support (should be move up to EDPluginExecProcess)
        - The list of pre-execution commands
        - The script command line that invokes the executable, which is written into the script
        (the EDPluginExecProcess command line is not used, but will be in the future: It will consist of the
        execProcessExecutable and the path to the script file.)
        - The list of execution commands for the execProcessScriptExecutable
        - The list of post-execution commands
        - The script base name (<date>-<random number>-<base name>)
        - The script file name
        - The script file path
        - The standard output log file name
        - The error output file log file name
        - The poll sleep time for checking if the process has finished (set to 1 s).
    """

    CONF_EXEC_PROCESS_SCRIPT_SHELL = "execProcessScriptShell"
    CONF_EXEC_PROCESS_SCRIPT_EXECUTOR = "execProcessScriptExecutor"
    CONF_EXEC_PROCESS_SCRIPT_EXECUTABLE = "execProcessScriptExecutable"
    CONF_EXEC_PROCESS_SCRIPT_SETUP_CCP4 = "execProcessScriptSetupCCP4"
    CONF_EXEC_PROCESS_SCRIPT_VERSION_STRING = "execProcessScriptVersionString"
    START_OF_ENVIRONMENT = "EDNA_START_OF_ENVIRONMENT"

    def __init__ (self):
        """
        Initializes process related attributes described above
        """
        EDPluginExecProcess.__init__(self)
        self.__strConfigShell = "/bin/bash"
        self.__strScriptExecutor = None
        self.__strScriptExecutable = None
        self.__strConfigSetupCCP4 = None
        self.__strVersion = None
        self.__listCompatibleVersions = []
        self.__strScriptCommandline = ""
        self.__strScriptBaseName = None
        self.__strScriptLogFileName = None
        self.__strScriptErrorLogFileName = None
        self.__strScriptFileName = None
        self.__bRequireCCP4 = False
        self.__listCommandPreExecution = []
        self.__listCommandExecution = []
        self.__listCommandPostExecution = []
        self.__iPollScriptProcessTime = 1 # [s]
        self.__strPathToHostNamePidFile = None
        self.__iNumberOfLastLinesFromLogFileIfError = 15


    def preProcess(self, _edObject=None):
        """
        Calls the parent preProcess method
        Generates the script
        """
        EDPluginExecProcess.preProcess(self)
        self.DEBUG("EDPluginExecProcessScript.preProcess")
        # The generateScript method will be called at the end of the preProcess method
        self.connectPreProcess(self.generateScript)


    def generateScript(self, _edObject=None):
        """
        This method prepares the script and writes it to disk.
        """
        strScript = self.prepareScript()
        self.writeExecutableScript(strScript)


    def process(self, _edObject=None):
        """
        This method starts the execution of the EDNA script using EDActionExecuteSystemCommand
        In case of failure, an error message is added to the list and the plugin fails.
        """
        EDPluginExecProcess.process(self)
        self.DEBUG("EDPluginExecProcessScript.process starting")
        self.synchronizeOn()
        if "TIMEOUT" in EDUtilsFile.readFile(self.__strPathToHostNamePidFile):
            self.error("Timeout message found in %s" % self.__strPathToHostNamePidFile)
            self.hasTimedOut(True)

        bTimeOut = self.isTimeOut()
        if bTimeOut == True:
            self.DEBUG("EDPluginExecProcessScript.process ========================================= ERROR! ================")
            strErrorMessage = "%s execution timed out ( > %.1f s)!" % (self.__strScriptExecutable, float(self.getTimeOut()))
            self.error(strErrorMessage)
            self.addErrorMessage(strErrorMessage)
            self.setFailure()
            strExecutionStatus = "timeout"
            if self.isVerboseDebug():
                raise RuntimeError(strErrorMessage)
        else:
            strExecutionStatus = self.getExecutionStatus()
            # Report an error if the result is not "0" and the result is not an empty string
            if not strExecutionStatus == "0" and not strExecutionStatus == "":
                self.DEBUG("EDPluginExecProcessScript.process ========================================= ERROR! ================")
                # Add any messages in the error log file (.err) to the list of error messages
                strErrorLog = self.readProcessErrorLogFile()
                if strErrorLog is None:
                    strErrorMessage = "%s execution error - status : %s" % (self.getClassName(), strExecutionStatus)
                    self.error(strErrorMessage)
                    self.addErrorMessage(strErrorMessage)
                    self.setFailure()
                    if self.isVerboseDebug():
                        raise RuntimeError(strErrorMessage)
                else:
                    strErrorMessage = "%s execution error : %s" % (self.getClassName(), strErrorLog)
                    self.error(strErrorMessage)
                    self.addErrorMessage(strErrorMessage)
                    self.setFailure()
                    if self.isVerboseDebug():
                        raise RuntimeError(strErrorMessage)
                # Add any messages in the log file (.log) to the list of error messages
                strLog = self.readProcessLogFile()
                if strLog is not None:
                    # Cut down the log file to the last part if it's long
                    listLogLines = strLog.split("\n")
                    if len(listLogLines) > self.__iNumberOfLastLinesFromLogFileIfError:
                        strErrorMessage = "Last part of the %s log file:" % self.__strScriptExecutable
                        self.ERROR(strErrorMessage)
                        self.addErrorMessage(strErrorMessage)
                        listLogLastLines = listLogLines[-self.__iNumberOfLastLinesFromLogFileIfError:]
                        strLogLastLines = ""
                        for strLine in listLogLastLines:
                            strLogLastLines += strLine + "\n"
                        self.ERROR(strLogLastLines)
                        self.addErrorMessage(strLogLastLines)
                        strMessage = "Please inspect log file: %s" % os.path.join(self.getWorkingDirectory(), self.getScriptLogFileName())
                        self.ERROR(strMessage)
                        self.addErrorMessage(strMessage)
                    else:
                        strMessage = "%s log file: \n%s" % (self.__strScriptExecutable, strLog)
                        self.ERROR(strMessage)
                        self.addErrorMessage(strMessage)
        #       Save the return code of the external program in the PID file
        open(self.__strPathToHostNamePidFile, "a").write(strExecutionStatus + os.linesep)

        self.DEBUG("EDPluginExecProcessScript.process finished ")
        self.synchronizeOff()


    def postProcess(self, _edObject=None):
        """
        Calls the parent preProcess method
        Checks that the installed 3rd party software is in the list of compatible versions
        """
        EDPluginExecProcess.postProcess(self)
        self.DEBUG("EDPluginExecProcessScript.postProcess")

        # Tests the compatibles executable versions
        listCompatibleVersions = self.getListOfCompatibleVersions()

        if(len(listCompatibleVersions) != 0):

            bFound = False
            for compatibleVersion in listCompatibleVersions:
                bFound = self.findStringInLog(compatibleVersion)
                if(bFound == True):
                    break

            if(bFound == False):
                strErrorMessage = "Plugin not compatible with %s, compatible versions are: %s" % (self.getStringVersion(), self.getCompatibleVersionsStringLine())
                self.error(strErrorMessage)
                self.addErrorMessage(strErrorMessage)
                self.setFailure()
                if self.isVerboseDebug():
                    raise RuntimeError, strErrorMessage



    def configure(self):
        """
        Configures the plugin from the configuration file with the following parameters
         - The shell that will execute the script
         - Script executor
         - Script executable to be invoked
         - Path to CCP4 setup file if required
         - The 3rd party executable installed version
        """
        EDPluginExecProcess.configure(self)
        self.DEBUG("EDPluginExecProcessScript.configure")
        strShell = self.config.get(self.CONF_EXEC_PROCESS_SCRIPT_SHELL)
        if strShell is None:
            self.DEBUG("EDPluginExecProcessScript.configure: No configuration parameter found for: " + \
                            self.CONF_EXEC_PROCESS_SCRIPT_SHELL + ", using default value: " + self.getScriptShell())
        else:
            self.setScriptShell(strShell)
        strScriptExecutor = self.config.get(self.CONF_EXEC_PROCESS_SCRIPT_EXECUTOR)
        if strScriptExecutor is None:
            self.setScriptExecutor(self.getScriptShell())
            self.DEBUG("EDPluginExecProcessScript.configure: No configuration parameter found for: " + \
                            self.CONF_EXEC_PROCESS_SCRIPT_EXECUTOR + ", using script shell: " + self.getScriptShell())
        else:
            self.setScriptExecutor(strScriptExecutor)
        if self.__strScriptExecutable is None:
            strScriptExecutable = self.config.get(self.CONF_EXEC_PROCESS_SCRIPT_EXECUTABLE)
            if strScriptExecutable is None:
                strErrorMessage = "Configuration parameter %s missing for plugin %s with EDNA_SITE=%s" % \
                                    (self.CONF_EXEC_PROCESS_SCRIPT_EXECUTABLE, \
                                      self.getPluginName(), EDUtilsPath.EDNA_SITE)
                self.error(strErrorMessage)
                self.addErrorMessage(strErrorMessage)
                self.setFailure()
                if self.isVerboseDebug():
                    raise RuntimeError, strErrorMessage
            else:
                # Check that the executable file exists
                if not os.path.exists(strScriptExecutable):
                    strErrorMessage = "Cannot find configured executable %s: %s for plugin %s with EDNA_SITE=%s" % \
                                    (self.CONF_EXEC_PROCESS_SCRIPT_EXECUTABLE, strScriptExecutable, \
                                      self.getPluginName(), EDUtilsPath.EDNA_SITE)
                    self.error(strErrorMessage)
                    self.addErrorMessage(strErrorMessage)
                    self.setFailure()
                    if self.isVerboseDebug():
                        raise RuntimeError, strErrorMessage
                else:
                    self.setScriptExecutable(strScriptExecutable)
        if not self.__strScriptExecutable:
            self.error("No executable found for plugin %s with EDNA_SITE=%s" % (self.getClassName(), EDUtilsPath.EDNA_SITE))

        strConfigSetupCCP4 = self.config.get(self.CONF_EXEC_PROCESS_SCRIPT_SETUP_CCP4)
        if strConfigSetupCCP4 is None:
            self.DEBUG("EDPluginExecProcessScript.configure: No configuration parameter found for: " + \
                            self.CONF_EXEC_PROCESS_SCRIPT_SETUP_CCP4 + ", NO default value!")
        else:
            self.setSetupCCP4(strConfigSetupCCP4)
        strVersion = self.config.get(self.CONF_EXEC_PROCESS_SCRIPT_VERSION_STRING)
        if strVersion is None:
            self.DEBUG("EDPluginExecProcessScript.configure: No configuration parameter found for: " + \
                            self.CONF_EXEC_PROCESS_SCRIPT_VERSION_STRING + ", NO default value!")
        else:
            self.setStringVersion(strVersion)

        if self.__strScriptBaseName is None:
            self.setScriptBaseName(self.getBaseName())
        if self.__strScriptFileName is None:
            self.setScriptFileName(self.__strScriptBaseName + ".sh")
        if self.__strScriptLogFileName is None:
            self.setScriptLogFileName(self.__strScriptBaseName + ".log")
        if self.__strScriptErrorLogFileName is None:
            self.setScriptErrorLogFileName(self.__strScriptBaseName + ".err")
        if self.__strScriptExecutable is not None:
            self.__strPathToHostNamePidFile = os.path.join(self.getWorkingDirectory(), os.path.basename(self.__strScriptExecutable) + "_hostNamePid.txt")


    def prepareScript(self):
        """
        Returns a string containing the script.
        """
        strScript = None
        self.DEBUG("EDPluginExecProcessScript.prepareScript")
        if "sh" in self.getScriptShell():
            strScript = self.prepareShellScript()
        elif "python" in self.getScriptShell():
            if self.__strScriptFileName.endswith(".sh"):
                self.setScriptFileName(self.__strScriptFileName[:-3] + ".py")
            strScript = self.preparePythonScript()
        elif "cmd" in self.getScriptShell():
            if self.__strScriptFileName.endswith(".sh"):
                self.setScriptFileName(self.__strScriptFileName[:-3] + ".bat")
            strScript = self.prepareBatchScript()
        return strScript

    def prepareShellScript(self):
        """
        Returns a string containing the Shell script.
        """
        self.DEBUG("EDPluginExecProcessScript.prepareShellScript")
        listScript = ["#!%s" % self.getScriptShell(),
                      "cd " + self.getWorkingDirectory()]
        if self.__bRequireCCP4:
            if self.__strConfigSetupCCP4 == None or self.__strConfigSetupCCP4 == "":
                self.DEBUG("EDPluginExecProcessScript.prepareShellScript : CCP4 setup script not defined.")
            else:
                listScript.append(". " + self.__strConfigSetupCCP4)
        # Add pre-execution commands - if any
        for strCommandPreExecution in self.__listCommandPreExecution:
            listScript.append(strCommandPreExecution)
        # Execution
        strScript = self.__strScriptExecutable + " " + self.__strScriptCommandline + " > " + self.__strScriptLogFileName + " 2> " + self.__strScriptErrorLogFileName
        # Add execution commands - if any
        if self.__listCommandExecution == []:
            strScript += " &"
            listScript.append(strScript)
        else:
            strScript += " << EOF-EDPluginExecProcessScript &"
            listScript.append(strScript)
            for strCommandExecution in self.__listCommandExecution:
                listScript.append(strCommandExecution)
            listScript.append("EOF-EDPluginExecProcessScript")

        listScript.append("ednaJobPid=$!")
        listScript.append("ednaJobHostName=$(hostname)")
        listScript.append('echo "$ednaJobHostName $ednaJobPid" > %s' % self.__strPathToHostNamePidFile)
        listScript.append("wait $ednaJobPid")
        # Add post-execution commands - if any
        for strCommandPostExecution in self.__listCommandPostExecution:
            listScript.append(strCommandPostExecution)
        listScript.append("")
        return os.linesep.join(listScript)


    def preparePythonScript(self):
        """
        Returns a string containing the Python script.
        """
        self.DEBUG("EDPluginExecProcessScript.preparePythonScript")

        #when running python script allow 1s+1% gracetime to let the python scripting mechanism to finish
        iScriptTimeOut = max(1, self.getTimeOut())
        self.setTimeOut(1 + 1.05 * iScriptTimeOut)
        self.DEBUG("Original Timeout is %s setting to %s" % (iScriptTimeOut, self.getTimeOut()))

        listScript = ["#!%s" % sys.executable, ""]

        listScript += ["import os, sys, subprocess, threading, socket, signal", "",
                      "os.chdir('%s')" % EDUtilsPlatform.escape(self.getWorkingDirectory()), "",
                      "def writeStdOutErr(std,filename):",
                      "        open(filename,'wb').write(std.read())",
                      "",
                      "def kill(pid):",
                      "    sys.stderr.write('TIMEOUT of %s pid: '+str(pid)+os.linesep)" %
                            EDUtilsPlatform.escape(self.__strScriptExecutable),
                      "    open('%s','a').write('TIMEOUT after %ss %s')" %
                            (EDUtilsPlatform.escape(self.__strPathToHostNamePidFile),
                            iScriptTimeOut, EDUtilsPlatform.escapedLinesep),
                      ]
        if EDUtilsPlatform.name == "nt":
            listScript += ["    os.kill(pid,signal.SIGTERM)",
                         "    sys.exit(-signal.SIGTERM)", ""]
        else:
            listScript += ["    os.kill(pid,signal.SIGKILL)",
                         "    sys.exit(-signal.SIGKILL)", ""]

        # Add pre-execution commands - if any
        cmdline = ""
        if self.__bRequireCCP4:
            if self.__strConfigSetupCCP4 == None or self.__strConfigSetupCCP4 == "":
                self.DEBUG("EDPluginExecProcessScript.preparePythonScript : CCP4 setup script not defined.")
            else:
                cmdline += ". %s %s" % (self.__strConfigSetupCCP4, EDUtilsPlatform.cmdSep)

        for strCommandPreExecution in self.__listCommandPreExecution:
            if strCommandPreExecution.strip().endswith("&"):
                cmdline += strCommandPreExecution
            else:
                cmdline += strCommandPreExecution + EDUtilsPlatform.cmdSep
        if len(cmdline) > 2:
            listScript += ["def getEnvironment(filename):",
                      "    dictEnv=None",
                      "    for oneFullLine in open(filename,'rb').readlines():",
                      "        oneLine=oneFullLine.strip()",
                      "        if ('=' in oneLine) and (isinstance(dictEnv,dict)):",
                      "            key,value = oneLine.split('=',1)",
                      "            dictEnv[key]=value",
                      "        elif oneLine == '%s':" % EDPluginExecProcessScript.START_OF_ENVIRONMENT,
                      "            dictEnv={}",
                      "    return dictEnv",
                      ""
                      ]

            cmdline += "echo %secho %s%s%s" % (EDUtilsPlatform.cmdSep,
                                                EDPluginExecProcessScript.START_OF_ENVIRONMENT,
                                                EDUtilsPlatform.cmdSep,
                                                EDUtilsPlatform.cmdEnv)
            listScript += ['subPre = subprocess.Popen("""%s""",shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)' % cmdline,
                           'threadStdErr = threading.Thread(target=writeStdOutErr, name="PreExecuteWriteStdErr", args=(subPre.stderr,"preExecute.err"))',
                           'threadStdOut = threading.Thread(target=writeStdOutErr, name="PreExecuteWriteStdOut", args=(subPre.stdout,"preExecute.log"))',
                           'threadStdErr.start()',
                           'threadStdOut.start()',
                           'threadStdErr.join()',
                           'threadStdOut.join()',
                           'subPre.wait()',
                           'dictEnv=getEnvironment("preExecute.log")']
        else:
            listScript.append('dictEnv=os.environ')

#        # Execution
        listScript.append("")

        strcmd = "%s %s" % (
            EDUtilsPlatform.escape(self.__strScriptExecutable),
            EDUtilsPlatform.escape(self.__strScriptCommandline))

        listCommandLine = shlex.split(str(strcmd))
        if self.__listCommandExecution == []:
            listScript.append('subP = subprocess.Popen(%s,stdout=subprocess.PIPE, stderr=subprocess.PIPE, env=dictEnv)' % listCommandLine)
        else:
            listScript.append('subP = subprocess.Popen(%s, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, env=dictEnv)' % listCommandLine)
            for strCommandExecution in self.__listCommandExecution:
                listScript.append('subP.stdin.write("%s%s")' % (strCommandExecution,
                                            EDUtilsPlatform.escapedLinesep))
            listScript.append('subP.stdin.close()')
        listScript += ['timer = threading.Timer(%s,kill,args=(subP.pid,))' % (iScriptTimeOut),
                       'timer.start()',
                       'open("%s","wb").write("%%s %%s %%s"%%(subP.pid,socket.gethostname(),os.linesep)) ' %
                                EDUtilsPlatform.escape(self.__strPathToHostNamePidFile),
                       'threadStdErr = threading.Thread(target=writeStdOutErr, name="WriteStdErr", args=(subP.stderr,"%s"))' %
                                EDUtilsPlatform.escape(self.__strScriptErrorLogFileName),
                       'threadStdOut = threading.Thread(target=writeStdOutErr, name="WriteStdOut", args=(subP.stdout,"%s"))' %
                                EDUtilsPlatform.escape(self.__strScriptLogFileName),
                       'threadStdErr.start()',
                       'threadStdOut.start()',
                       'threadStdErr.join()',
                       'threadStdOut.join()',
                       'subP.wait()',
                       'timer.cancel()'
                       '']
        # Add post-execution commands - if any
        cmdline = ""
        for strCommandPostExecution in self.__listCommandPostExecution:
            if strCommandPostExecution.strip().endswith(" & "):
                cmdline += strCommandPostExecution
            else:
                cmdline += strCommandPostExecution + EDUtilsPlatform.cmdSep

            listScript.append('subPost = subprocess.Popen("""%s""", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, env=dictEnv)' % cmdline)
            listScript.append('threadStdErr = threading.Thread(target=writeStdOutErr, name="PreExecuteWriteStdErr", args=(subPost.stderr,"postExecute.log"))')
            listScript.append('threadStdOut = threading.Thread(target=writeStdOutErr, name="PreExecuteWriteStdOut", args=(subPost.stdout,"postExecute.err"))')
            listScript.append('threadStdErr.start()')
            listScript.append('threadStdOut.start()')
            listScript.append('threadStdErr.join()')
            listScript.append('threadStdOut.join()')
            listScript.append('subPost.wait()')


        listScript.append("sys.exit(subP.returncode)")
        listScript.append("")
        strPythonScript = os.linesep.join(listScript)
        return strPythonScript



    def prepareBatchScript(self):
        """
        Returns a string containing the windows batch script.
        """

        self.DEBUG("EDPluginExecProcessScript.prepareBatchScript")
        listScript = ["@ECHO OFF",
                      "cd " + self.getWorkingDirectory()]

        # Add pre-execution commands - if any
        for strCommandPreExecution in self.__listCommandPreExecution:
            listScript.append(strCommandPreExecution)
        # Execution
        # Add execution commands - if any
        if self.__strScriptExecutable.endswith(".bat") or self.__strScriptExecutable.endswith(".cmd") :
            strExecutable = "@CALL " + self.__strScriptExecutable
        else:
            strExecutable = self.__strScriptExecutable
        if self.__listCommandExecution == []:
            listScript.append("'%s' '%s' > '%s' 2> '%s' &" % (strExecutable , self.__strScriptCommandline , self.__strScriptLogFileName, self.__strScriptErrorLogFileName))
        else:
            for  strCommandExecution in self.__listCommandExecution:
                listScript.append("echo %s >>EDNA_StdInput.txt" % strCommandExecution)

            listScript.append("'%s' '%s' < EDNA_StdInput.txt > '%s' 2> '%s' &" % (self.__strScriptExecutable , self.__strScriptCommandline , self.__strScriptLogFileName, self.__strScriptErrorLogFileName))

        listScript.append('for /F "token=2" %I in (\' TASKLIST /NH /FI "IMAGENAME eq  %s " \')DO SET PID=%I' % os.path.basename(self.__strScriptExecutable))
        listScript.append('hostname> %s' % self.__strPathToHostNamePidFile)
        listScript.append('echo %PID% > %s' % self.__strPathToHostNamePidFile)
#        listScript.append("wait $ednaJobPid")
        # Add post-execution commands - if any
        for strCommandPostExecution in self.__listCommandPostExecution:
            listScript.append(strCommandPostExecution)
        listScript.append("")
        return os.linesep.join(listScript)


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


    def setRequireCCP4(self, _bReqireCCP4):
        """
        Sets a requirement on CCP4
        """
        self.synchronizeOn()
        self.__bRequireCCP4 = _bReqireCCP4
        self.synchronizeOff()


    def getRequireCCP4(self):
        """
        Returns True if the executable requires CCP4
        """
        return self.__bRequireCCP4


    def setListCommandExecution(self, _listCommandExecution):
        """
        Sets the list of execution commands
        """
        self.synchronizeOn()
        if _listCommandExecution is not None:
            self.__listCommandExecution = list(_listCommandExecution)
        self.synchronizeOff()


    def addListCommandExecution(self, _strCommandExecution):
        """
        Adds an execution command to the list
        """
        self.synchronizeOn()
        if _strCommandExecution is not None:
            self.__listCommandExecution.append(_strCommandExecution)
        self.synchronizeOff()


    def getListCommandExecution(self):
        """
        Returns the list of execution commands
        """
        self.synchronizeOn()
        edObject = None
        if self.__listCommandExecution is not None:
            edObject = list(self.__listCommandExecution)
        self.synchronizeOff()
        return edObject


    def setListCommandPreExecution(self, _listCommandPreExecution):
        """
        Sets the list of pre execution commands
        """
        self.synchronizeOn()
        if _listCommandPreExecution is not None:
            self.__listCommandPreExecution = list(_listCommandPreExecution)
        self.synchronizeOff()


    def addListCommandPreExecution(self, _strCommandPreExecution):
        """
        Adds a pre execution command to the list
        """
        self.synchronizeOn()
        if _strCommandPreExecution is not None:
            self.__listCommandPreExecution.append(_strCommandPreExecution)
        self.synchronizeOff()


    def getListCommandPreExecution(self):
        """
        Returns the list of pre execution commands
        """
        self.synchronizeOn()
        edObject = None
        if self.__listCommandPreExecution != None:
            edObject = list(self.__listCommandPreExecution)
        self.synchronizeOff()
        return edObject


    def setListCommandPostExecution(self, _listCommandPostExecution):
        """
        Sets the list of post execution commands
        """
        self.synchronizeOn()
        if _listCommandPostExecution is not None:
            self.__listCommandPostExecution = list(_listCommandPostExecution)
        self.synchronizeOff()


    def addListCommandPostExecution(self, _strCommandPostExecution):
        """
        Adds a post execution command to the list
        """
        self.synchronizeOn()
        if _strCommandPostExecution is not None:
            self.__listCommandPostExecution.append(_strCommandPostExecution)
        self.synchronizeOff()


    def getListCommandPostExecution(self):
        """
        Returns the list of post execution commands
        """
        self.synchronizeOn()
        edObject = None
        if self.__listCommandPostExecution != None:
            edObject = list(self.__listCommandPostExecution)
        self.synchronizeOff()
        return edObject


    def setScriptShell(self, _strScriptShell):
        """
        Sets the script shell
        """
        self.synchronizeOn()
        self.__strConfigShell = _strScriptShell
        self.synchronizeOff()


    def getScriptShell(self):
        """
        Returns the script shell
        """
        return self.__strConfigShell


    def setScriptExecutor(self, _strScriptExecutor):
        """
        Sets the script executor
        """
        self.synchronizeOn()
        self.__strScriptExecutor = _strScriptExecutor
        self.synchronizeOff()


    def getScriptExecutor(self):
        """
        Returns the script executor
        """
        return self.__strScriptExecutor


    def setSetupCCP4(self, _strSetupCCP4):
        """
        Sets the path to CCP4 setup file
        """
        self.synchronizeOn()
        self.__strConfigSetupCCP4 = _strSetupCCP4
        self.synchronizeOff()


    def getSetupCCP4(self):
        """
        Returns the path to CCP4 setup file
        """
        return self.__strConfigSetupCCP4


    def setScriptBaseName(self, _strScriptBaseName):
        """
        Sets the script name
        """
        self.synchronizeOn()
        self.__strScriptBaseName = _strScriptBaseName
        self.synchronizeOff()


    def getScriptBaseName(self):
        """
        Returns the script name 
        if None, create it: <date>-<random number>-<base name>
        """
        if self.__strScriptBaseName is None:
            self.__strScriptBaseName = self.createBaseName()
        return self.__strScriptBaseName


    def setScriptLogFileName(self, _strScriptLogFileName):
        """
        Sets the standard output log file name
        """
        self.synchronizeOn()
        self.__strScriptLogFileName = _strScriptLogFileName
        self.synchronizeOff()


    def setScriptErrorLogFileName(self, _strScriptErrorLogFileName):
        """
        Sets the error output log file name
        """
        self.synchronizeOn()
        self.__strScriptErrorLogFileName = _strScriptErrorLogFileName
        self.synchronizeOff()


    def getScriptLogFileName(self):
        """
        Returns the standard output log file name
        """
        return self.__strScriptLogFileName


    def getScriptErrorLogFileName(self):
        """
        Returns the error output log file name
        """
        return self.__strScriptErrorLogFileName


    def setScriptFileName(self, _strScriptFileName):
        """
        Sets the script file name
        """
        self.synchronizeOn()
        self.__strScriptFileName = _strScriptFileName
        self.synchronizeOff()


    def getScriptFileName(self):
        """
        Returns the script file name
        """
        return self.__strScriptFileName


    def getScriptFilePath(self):
        """
        Returns the script file path
        """
        return os.path.join(self.getWorkingDirectory(), self.__strScriptFileName)


    def setScriptExecutable(self, _strScriptExecutable):
        """
        Sets the executable path
        """
        with self.locked():
            self.__strScriptExecutable = _strScriptExecutable

    def getScriptExecutable(self):
        """
        Returns the executable path
        """
        return self.__strScriptExecutable
    scriptExecutable = property(getScriptExecutable, setScriptExecutable)

    def setScriptCommandline(self, _strScriptCommandline):
        """
        Sets the script command line (parameters to executable)
        """
        self.synchronizeOn()
        self.__strScriptCommandline = _strScriptCommandline
        self.synchronizeOff()


    def getScriptCommandline(self):
        """
        Returns the script command line (parameters to executable)
        """
        return self.__strScriptCommandline


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
        if self.__strVersion is not None:
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




    def writeExecutableScript(self, _strScript):
        """
        Writes the script to the script file.
        """
        self.DEBUG("EDPluginExecProcessScript.writeScriptToFile")
        EDUtilsFile.writeFile(self.getScriptFilePath(), _strScript)
        self.setExecutable(self.getScriptExecutor())
        self.setCommandline(self.getScriptFilePath())


    def findStringInLog(self, _strInput):
        """
        Returns True if a string exists in the log file
        """
        self.DEBUG("EDPluginExecProcessScript.findStringInLog")
        bTestSuccess = False
        strLogFileContent = self.readProcessLogFile()
        if strLogFileContent.find(_strInput) != -1:
            bTestSuccess = True
        return bTestSuccess


    def testVersion(self):
        """
        Deprecated not used
        See postProcess for version checking
        """
        self.DEBUG("EDPluginExecProcessScript.testVersion")
        bCorrectVersion = False
        if self.findStringInLog(self.__strVersion) != None:
            bCorrectVersion = True
        return bCorrectVersion


    def writeProcessFile(self, _strFileName, _strContent):
        """
        Main method to write a file in the plugin working directory
        Such a file is called process file
        """
        self.DEBUG("EDPluginExecProcessScript.writeProcessFile")
        strFilePath = os.path.join(self.getWorkingDirectory(), _strFileName)
        EDUtilsFile.writeFile(strFilePath, _strContent)


    def readProcessFile(self, _strFileName):
        """
        Returns the file content of a process file
        """
        self.DEBUG("EDPluginExecProcessScript.readProcessFile")
        strFilePath = os.path.join(self.getWorkingDirectory(), _strFileName)
        strFileContent = None
        if os.path.exists(strFilePath):
            strFileContent = EDUtilsFile.readFile(strFilePath)
        return strFileContent


    def readProcessLogFile(self):
        """
        Returns the content of the process standard output log file
        """
        self.DEBUG("EDPluginExecProcessScript.readProcessLogFile")
        strLogFileContent = None
        if self.getScriptLogFileName() is not None:
            strLogFileContent = self.readProcessFile(self.getScriptLogFileName())
        return strLogFileContent


    def readProcessErrorLogFile(self):
        """
        Returns the content of the process error output log file
        """
        self.DEBUG("EDPluginExecProcessScript.readProcessErrorLogFile")
        strErrorLogFileContent = self.readProcessFile(self.getScriptErrorLogFileName())
        return strErrorLogFileContent

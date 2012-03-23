# coding: utf8
#
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

__authors__ = [ "Marie-Francoise Incardona", "Olof Svensson", "Jérôme Kieffer" ]
__contact__ = "svensson@esrf.fr"
__license__ = "LGPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"

import threading, shlex, sys

from EDVerbose          import EDVerbose
from EDPlugin           import EDPlugin
from EDPluginExec       import EDPluginExec
from EDConfiguration    import EDConfiguration
from EDMessage          import EDMessage
from EDUtilsPlatform    import EDUtilsPlatform

from XSDataCommon       import XSPluginItem

class EDPluginExecProcess(EDPluginExec):
    """
    The super class for all plugins that execute a process
    This class manages the process to be launched:
        - Process time out management (configurable by EDPlugin )
        - Process executable to be invoked (configurable, Default 'cat')
        - Process command line to be launched (Default: empty)
    The ExecProcess plugin is required to have a configuration in order 
    to be executed in a plugin execution test case.
    """

    CONF_EXEC_PROCESS_TIME_OUT = "execProcessTimeOut"
    CONF_EXEC_PROCESS_EXECUTABLE = "execProcessExecutable"

    def __init__ (self):
        """
        Initializes process related attributes described above
        """
        EDPluginExec.__init__(self)
        self.setRequiredToHaveConfiguration()
        self.__strConfigExecutable = "cat"
        self.__strConfigCommandline = ""
        self.__subprocess = None
        self.__iPID = None
        self.__strCWD = None
        self.__strExecutionStatus = ""


    def process(self, _edObject=None):
        """
        Sets the process up with the executable, command line and time out
        Launches the process, in case of error, an error message is added to the list, and the plugins fails 
        """
        EDPluginExec.process(self)
        EDVerbose.DEBUG("EDPluginExecProcess.process starting")
        strCommand = self.getExecutable() + " " + self.getCommandline()
        EDVerbose.DEBUG("EDPluginExecProcess.process executing: " + self.getExecutable())
        self.synchronizeOn()
        EDVerbose.screen(self.getBaseName() + ": Processing")
        timer = threading.Timer(float(self.getTimeOut()), self.kill)
        timer.start()
        self.__subprocess = EDUtilsPlatform.Popen(shlex.split(str(EDUtilsPlatform.escape(strCommand))),
                                                   cwd=self.getWorkingDirectory())
        self.__iPID = self.__subprocess.pid
        self.__strExecutionStatus = str(self.__subprocess.wait())
        timer.cancel()
        EDVerbose.DEBUG("EDPluginExecProcess.process finished ")
        self.synchronizeOff()


    def kill(self):
        EDVerbose.WARNING("I will kill subprocess %s pid= %s" % (self.__subprocess, self.__iPID))
        EDUtilsPlatform.kill(self.__iPID)
        self.synchronizeOff()
        self.__strExecutionStatus = "timeout"
        EDVerbose.DEBUG("EDPluginExecProcess.process ========================================= ERROR! ================")
        errorMessage = EDMessage.ERROR_EXECUTION_03 % ('EDPluginExecProcess.process', self.getClassName(), "Timeout ")
        EDVerbose.error(errorMessage)
        self.addErrorMessage(errorMessage)
        raise RuntimeError, errorMessage


    def configure(self):
        """
        Configures the plugin with executable from configuration file
        """
        EDPluginExec.configure(self)
        EDVerbose.DEBUG("EDPluginExecProcess.configure")
        xsPluginItem = self.getConfiguration()
        if (xsPluginItem == None):
            EDVerbose.warning("EDPluginExecProcess.configure: No plugin item defined.")
            xsPluginItem = XSPluginItem()
        strExecutable = EDConfiguration.getStringParamValue(xsPluginItem, EDPluginExecProcess.CONF_EXEC_PROCESS_EXECUTABLE)
        if(strExecutable == None):
            EDVerbose.DEBUG("EDPluginExecProcess.configure: No configuration parameter found for: %s , using default value: %s"\
                            % (EDPluginExecProcess.CONF_EXEC_PROCESS_EXECUTABLE, self.getExecutable()))
        else:
            self.setExecutable(strExecutable)
        # The execProcessTimeOut is deprecated, see bug #563
        strTimeOut = EDConfiguration.getStringParamValue(xsPluginItem, EDPluginExecProcess.CONF_EXEC_PROCESS_TIME_OUT)
        if strTimeOut is not None:
            EDVerbose.WARNING("Use of %s in plugin configuration is deprecated" % EDPluginExecProcess.CONF_EXEC_PROCESS_TIME_OUT)
            EDVerbose.WARNING("Please use %s instead." % EDPlugin.CONF_TIME_OUT)
            self.setTimeOut(strTimeOut)


    def setExecutable(self, _strExecutable):
        """
        Sets the executable
        """
        self.__strConfigExecutable = _strExecutable


    def getExecutable(self):
        """
        Sets the executable
        """
        if self.__strConfigExecutable == "python":
            return sys.executable
        return self.__strConfigExecutable


    def setCommandline(self, _strCommandline):
        """
        Sets the command line
        """
        self.__strConfigCommandline = _strCommandline


    def getCommandline(self):
        """
        Returns the command line
        """
        return self.__strConfigCommandline

    def getPid(self):
        return self.__iPID


    def getExecutionStatus(self):
        """
        Returns the string containing the execution status.
        """
        return self.__strExecutionStatus

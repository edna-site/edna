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

import threading, shlex, sys, time, subprocess

from EDVerbose          import EDVerbose
from EDPlugin           import EDPlugin
from EDPluginExec       import EDPluginExec
from EDConfiguration    import EDConfiguration
from EDMessage          import EDMessage
from EDUtilsPlatform    import EDUtilsPlatform

from XSDataCommon       import XSPluginItem

OAR_POLL_COMMAND = 'oarstat -s -j {0:d}'
DEFAULT_OAR_POLL_INTERVAL = 10

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


    def process_locally(self, _edObject=None):
        """
        Sets the process up with the executable, command line and time out
        Launches the process, in case of error, an error message is added to the list, and the plugins fails
        """
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


    def process_on_oar(self, _edObject=None):
        """
        Special processing method for OAR. Since oarsub returns
        immediately we cannot rely on Popen.wait(). Instead we'll poll
        the cluster using the oarstat utility. In order to do that
        we'll setup a timer firing at regular intervals until we're
        done or the total time exceeds the timeout config parameter.
        """
        if self._oar_options is not None:
            command = '{0} {1} {2}'.format(self.getExecutable(),
                                       self._oar_options,
                                       self.getCommandline())
        else:
            command = '{0} {1}'.format(self.getExecutable(), self.getCommandline())
        EDVerbose.DEBUG('EDPluginExecProcess.process_on_oar executing: "{0}"'.format(command))
        self._start_time = time.time()
        self._timer = threading.Timer(float(self._oar_poll_interval), self.poll_oar)
        oarsub = subprocess.Popen(shlex.split(EDUtilsPlatform.escape(command)),
                                  cwd=self.getWorkingDirectory(),
                                  stdout=subprocess.PIPE)
        oar_job_id = None
        for line in oarsub.stdout:
            if line.startswith('OARJOB_ID='):
                oar_job_id = int(line.split()[1])
        if oar_job_id is not None:
            EDVerbose.DEBUG('EDPluginExecProcess.process_on_oar: job id is "{0}"'.format(oar_job_id))
            self._oar_job_id = oar_job_id
        else:
            msg = 'EDPluginExecProcess.process_on_oar: could not get OAR_JOB_ID!'
            EDVerbose.ERROR(msg)
            self.addErrorMessage(msg)
            raise RuntimeError(msg)


    def poll_oar(self):
        command = OAR_POLL_COMMAND.format(self._oar_job_id)
        EDVerbose.DEBUG('EDPluginExecProcess.poll_oar: polling oar with "{0}"'.format(command))

        oarstat = subprocess.Popen(shlex.split(command),
                                   cwd=self.getWorkingDirectory(),
                                   stdout=subprocess.PIPE)
        status = None
        for line in oarstat.stdout:
            if line.startswith(str(self._oar_job_id)):
                status = line.split()[-2]
                break
        if status is None:
            msg = 'EDPluginExecProcess.poll_oar: could not get job status for job {0:d}'.format(self._oar_job_id)
            EDVerbose.WARNING(msg)
            self.addErrorMessage(msg)
            raise RuntimeError(msg)
        elif status == 'Terminated':
            EDVerbose.DEBUG('EDPluginExecProcess.poll_oar: job {0:i} finished'.format(self._oar_job_id))
        elif status == 'Running':
            EDVerbose.DEBUG('EDPluginExecProcess.poll_oar: job {0:i} still running'.format(self._oar_job_id))
        else:
            msg = 'EDPluginExecProcess.poll_oar: job {0:i} in a non handled state'.format(self._oar_job_id)
            EDVerbose.DEBUG(msg)
            self.addErrorMessage(msg)
            raise RuntimeError(msg)

        # we must then decide if we continue for another polling round
        if time.time() - self._start_time >= self.getTimeOut():
            msg = 'EDPluginExecProcess.poll_oar: timeout!'
            EDVerbose.ERROR(msg)
            self.addErrorMessage(msg)
            raise RuntimeError(msg)
        else:
            self._timer = threading.Timer(self._oar_poll_interval, self.poll_oar)
            self._timer.start()


    def process(self, _edObject=None):
        EDPluginExec.process(self)
        EDVerbose.DEBUG("EDPluginExecProcess.process starting")
        if self.getExecutable() == "oarsub":
            self.process_on_oar(_edObject)
        else:
            self.process_locally(_edObject)


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
        strExecutable = self.config.get(self.CONF_EXEC_PROCESS_EXECUTABLE, None)
        if strExecutable is None:
            EDVerbose.DEBUG("EDPluginExecProcess.configure: No configuration parameter found for: %s , using default value: %s"\
                            % (self.CONF_EXEC_PROCESS_EXECUTABLE, self.getExecutable()))
        else:
            self.setExecutable(strExecutable)

        # test if we're to use oar and check for additional config
        if strExecutable == "oarsub":
            oar_options = self.config.get("oarOptions", None)
            if oar_options is None:
                EDVerbose.DEBUG('EDPluginExecProcess.configure: no additional options were specified for oarsub')
            self._oar_options = oar_options
            oar_poll = self.config.get("oarPollInterval", None)
            if oar_poll is None:
                EDVerbose.DEBUG('EDPluginExecProcess.configure: oar polling interval not configured')
                EDVerbose.DEBUG('EDPluginExecProcess.configure: using default version of {0}'.format(DEFAULT_OAR_POLL_INTERVAL))
                self._oar_poll_interval = DEFAULT_OAR_POLL_INTERVAL
            else:
                self._oar_poll_interval = oar_poll

        # The execProcessTimeOut is deprecated, see bug #563
        timeOut = self.config.get(self.CONF_EXEC_PROCESS_TIME_OUT, None)
        if timeOut is not None:
            EDVerbose.WARNING("Use of %s in plugin configuration is deprecated" % self.CONF_EXEC_PROCESS_TIME_OUT)
            EDVerbose.WARNING("Please use %s instead." % EDPlugin.CONF_TIME_OUT)
            self.setTimeOut(timeOut)


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

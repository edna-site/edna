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


__authors__ = [ "Marie-Francoise Incardona", "Olof Svensson", "Jerome Kieffer" ]
__contact__ = "svensson@esrf.fr"
__license__ = "LGPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"

"""
This class is used for executing and controlling external applications 
such as scripts.
"""


import os, subprocess, signal

from EDAction import EDAction
from EDVerbose import EDVerbose



class EDActionExecuteSystemCommand(EDAction):
    """
    This class executes a process using the Python os.sytem command.
    It is a temporary solution for the "==>[ERROR]: OSError: [Errno 10] No child processes"
    problem with ALActionProcess (Python bug in subprocess, see bug #61).
    """


    def __init__(self, _strCommand):
        """
        Initializes the class: the argument _strCommand should be
        the complete command line, i.e. path to executable + command line arguments
        """
        EDAction.__init__(self)
        self.__strCommand = _strCommand
        self.__strExecutionStatus = None
        self.__subprocess = None
        self.__iPID = None


    def process(self, _edPlugin=None):
        """
        Executes the command line using the standard Python os.system command.
        The result of the os.system command is converted into an str.
        """
        EDVerbose.DEBUG("*** EDActionExecuteSystemCommand.process")
        self.__subprocess = subprocess.Popen (self.__strCommand, shell=True)
        self.__iPID = self.__subprocess.pid
        executionStatus = self.__subprocess.wait()
        if (executionStatus is None):
            # If the status returned is None, return an empty string
            self.__strExecutionStatus = str()
        else:
            self.__strExecutionStatus = str(executionStatus)


    def getExecutionStatus(self):
        """
        Returns the string containing the execution status.
        """
        return self.__strExecutionStatus


    def abort(self, _edObject=None):
        """
        This method can be used to abort the process, for example when
        the execution time has exceeded the maximum allowed execution time.
        """
        EDVerbose.DEBUG("*** EDActionExecuteSystemCommand.abort")
        os.kill(self.__iPID, signal.SIGKILL)
        self.m_bIsAbort = True

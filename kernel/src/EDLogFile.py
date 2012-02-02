#
#    Project: The EDNA Kernel
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2008-2009 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal authors: Olof Svensson (svensson@esrf.fr) 
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

#
# This class has been inspired by the corresponding AALib class 
# (20090518-PyAALib-JyAALib-111) and modified according to the needs 
# for the EDNA project.
#

__author__ = "Olof Svensson"
__contact__ = "svensson@esrf.fr"
__license__ = "LGPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"

import time, threading, sys


class EDLogFile(object):
    """
    This file takes care of creating a log file and writes messages to the log file.
    """

    def __init__(self, _pyStrLogFileName=None):
        """
        @param _pyStrLogFileName: Optional path to or name of the log file.
        @type _pyStrLogFileName: python string 
        """
        self.__pyStrLogFileName = _pyStrLogFileName
        self.__pyFileLog = None
        self.__pyListLogCache = []
        self.__iMaxLogCache = 50
        self.__bIsLogFileOn = True


    def __createLogFile(self):
        """
        This private method creates the log file. If the log file name or path is not set
        a name of the type "EDNA_YYMMDD-HHMM.log" is used.
        """
        if (self.__bIsLogFileOn):
            if (self.__pyStrLogFileName is None):
                self.__pyStrLogFileName = "EDNA_%s.log" % time.strftime("%Y%m%d-%H%M%S", time.localtime(time.time()))
            self.__pyFileLog = file(self.__pyStrLogFileName, "w")
            for pyStrLogMessage in self.__pyListLogCache:
                self.write(pyStrLogMessage)


    def write(self, _pyStrLogMessage):
        """
        This method writes a message to the log file. If the log file name is not set
        messages are cached up to the limit __iMaxLogCache defined in the constructor.
        
        Once a file name of the log file has been defined all cached log messages are
        flushed to the log file.
        
        This allow log messages to be written to the log file even if the log messages
        are issued before the name of the log file has been determined by the EDNA
        application.
        
        @param _pyStrLogMessage: a log message
        @type _pyStrLogMessage: python string
        """
        if (self.__bIsLogFileOn):
            if (self.__pyFileLog is None):
                self.__pyListLogCache.append(_pyStrLogMessage)
                if (len(self.__pyListLogCache) > self.__iMaxLogCache):
                    self.__createLogFile()
            else:
                self.__pyFileLog.write(time.strftime("%Y%m%d-%H%M%S", time.localtime(time.time())) + _pyStrLogMessage)
                self.__pyFileLog.flush()


    def setLogFileName(self, _pyStrLogFilePath):
        """        
        @param _pyStrLogFilePath: The name or path of the log file
        @type _pyStrLogMessage: python string
        """
        self.__pyStrLogFileName = _pyStrLogFilePath
        self.__createLogFile()


    def setLogFileOff(self):
        """        
        This method turns off logging to a file. 
        """
        self.__bIsLogFileOn = False

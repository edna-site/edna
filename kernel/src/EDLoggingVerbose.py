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
from __future__ import with_statement

__authors__ = ["Olof Svensson", "Jérôme Kieffer"]
__contact__ = "svensson@esrf.fr"
__license__ = "LGPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"
__date__ = "2011-07-29"

import os, sys, traceback
from EDLogFile import EDLogFile
from EDThreading import Semaphore


class EDLoggingVerbose(object):
    """
    This class in the same as EDVerbose however it's not static.
    """

    def __init__(self):
        object.__init__(self)
        self.__pySemaphoreWrite = Semaphore()
        self.__bIsVerbose = True
        self.__bIsVerboseDebug = False
        self.__bIsTest = False
        self.__edLogFile = EDLogFile()


    def setLogLevel(self, _logLevel):
        pass

    def setAllLogLevels(self, _logLevel):
        pass

    def setTestOn(self):
        """
        turn on the test mode: all assertions become verbose (->screen) 
        """
        self.__bIsTest = True


    def setTestOff(self):
        """
        turn off the test mode: all assertions become silent (->screen) 
        """
        self.__bIsTest = False


    def setVerboseOn(self):
        """
        This method turns on verbose logging to standard output (stdout)
        """
        self.__bIsVerbose = True


    def setVerboseOff(self):
        """
        This method turns off verbose logging to standard output (stdout)
        """
        self.__bIsVerbose = False


    def setVerboseDebugOn(self):
        """
        This method turns on debug messages to standard output and log file
        """
        self.__bIsVerboseDebug = True


    def setVerboseDebugOff(self):
        """
        This method turns off debug messages to standard output and log file
        """
        self.__bIsVerboseDebug = False


    def isVerboseDebug(self):
        """
        This method returns the current status of debugging
        
        @return: if debug output to standard output and log file is enabled.
        @type: boolean
        """
        return self.__bIsVerboseDebug


    def __writeStdout(self, _strMessage=""):
        """
        A private thread safe method for writing a string to standard output and to log file
        
        @param _strMessage: The string to be written to standard output
        @type _strMessage: python string
        """
        with self.__pySemaphoreWrite:
            if (self.__bIsVerbose or self.__bIsVerboseDebug):
                sys.stdout.write(_strMessage)
            self.__edLogFile.write(_strMessage)


    def __writeStderr(self, _strMessage=""):
        """
        A private thread safe method for writing a string to standard error and to log file
        
        @param _strMessage: The string to be written to standard error
        @type _strMessage: python string
        """
        with self.__pySemaphoreWrite:
            if (self.__bIsVerbose or self.__bIsVerboseDebug):
                sys.stderr.write(_strMessage)
            self.__edLogFile.write(_strMessage)


    def log(self, _strMessage=""):
        """
        This method writes a message only to the log file.
        
        @param _strMessage: The string to be written to the log file
        @type _strMessage: python string
        """
        with self.__pySemaphoreWrite:
            self.__edLogFile.write("  %s%s" % (_strMessage, os.linesep))


    def screen(self, _strMessage=""):
        """
        This method writes a message to standard output and to the log file.
        
        @param _strMessage: The string to be written to the log file
        @type _strMessage: python string
        """
        self.__writeStdout("  %s%s" % (_strMessage, os.linesep))


    def DEBUG(self, _strDebugMessage=""):
        """
        This method writes a debug message to standard output and to the log file
        if debugging is enabled. The message will be written with the prefix [DEBUG]
        
        @param _strDebugMessage: The debug message to be written to standard output and log file
        @type _strDebugMessage: python string
        """
        if (self.__bIsVerboseDebug):
            self.__writeStdout("  [DEBUG]: %s%s" % (_strDebugMessage, os.linesep))


    def unitTest(self, _strMessage=""):
        """
        This method is meant to be used by the testing framework. The message will be written 
        to standard output and the log file with the prefix [UnitTest]
        
        @param _strMessage: The message to be written to standard output and log file
        @type _strMessage: python string
        """
        self.__writeStdout("  [UnitTest]: %s%s" % (_strMessage, os.linesep))


    def ERROR(self, _strMessage=""):
        """
        This method writes a message to standard error and the log file with the prefix [ERROR].
        
        @param _strMessage: The error message to be written to standard output and log file
        @type _strMessage: python string
        """
        self.__writeStderr("  [ERROR]: %s%s" % (_strMessage, os.linesep))


    def error(self, _strMessage=""):
        """
        This method writes a message to standard error and the log file with the prefix [ERROR].
        
        @param _strMessage: The error message to be written to standard output and log file
        @type _strMessage: python string
        """
        self.ERROR(_strMessage)


    def WARNING(self, _strMessage=""):
        """
        This method writes a warning message to standard output and the log file with the prefix [Warning].
        
        @param _strMessage: The error message to be written to standard output and log file
        @type _strMessage: python string
        """
        self.__writeStdout("  [Warning]: %s%s" % (_strMessage, os.linesep))


    def warning(self, _strMessage=""):
        """
        This method writes a warning message to standard output and the log file with the prefix [Warning].
        
        @param _strMessage: The error message to be written to standard output and log file
        @type _strMessage: python string
        """
        self.WARNING(_strMessage)


    def ASSERT(self, _strMessage):
        """
        This method writes an assert message to standard output and the log file with the prefix [ASSERT].
        
        @param _strMessage: The error message to be written to standard output and log file
        @type _strMessage: python string
        """
        if self.__bIsTest:
            self.screen("[ASSERT]:   %s" % _strMessage)
        else:
            self.log("[ASSERT]:   %s" % _strMessage)


    def writeErrorTrace(self, _strPrefix="  "):
        """
        This method writes an error trace to standard output and the log file. The error trace has
        the same formatting as normal Python error traces.
        
        @param _strPrefix: A prefix which can be customized, e.g. the testing framework uses '  [UnitTest]'
        @type _strPrefix: python string
        """
        (exc_type, exc_value, exc_traceback) = sys.exc_info()
        pyListTrace = traceback.extract_tb(exc_traceback)
        self.__writeStderr("%s Traceback (most recent call last): %s" % (_strPrefix, os.linesep))
        for pyListLine in pyListTrace:
            self.__writeStderr("%s  File \"%s\", line %d, in %s%s" % (_strPrefix, pyListLine[0],
                                                                                        pyListLine[1],
                                                                                        pyListLine[2],
                                                                                        os.linesep))
            self.__writeStderr("%s    %s%s" % (_strPrefix, pyListLine[3], os.linesep))
        strErrorMessage = traceback.format_exception_only(exc_type, exc_value)[0][:-1]
        self.__writeStderr(_strPrefix + strErrorMessage + os.linesep)


    def setLogFileName(self, _strLogFileName):
        """
        This method can be used for customising the file name of the log file.
        
        @param _strLogFileName: A file name for the log file.
        @type _strLogFileName: python string
        """
        self.__edLogFile.setLogFileName(_strLogFileName)


    def setLogFileOff(self):
        """
        This method truns off output to the log file.
        """
        self.__edLogFile.setLogFileOff()


    def __call__(self):
        #
        # Singleton!
        #
        return self

EDLoggingVerbose = EDLoggingVerbose()

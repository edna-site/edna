#
#    Project: The EDNA Kernel
#             http://www.edna-site.org
#
#    File: "$Id: EDImportLib.py 1453 2010-04-28 16:20:46Z svensson $"
#
#    Copyright (C) 2010-2010 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal authors: Olof Svensson (svensson@esrf.fr) 
#                       Mark Basham (Mark.Basham@diamon.ac.uk)
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
"""
EDLogging uses the standard python logging facility for providing
convenient methods for logging for all EDNA classes.
"""

__authors__ = ["Olof Svensson", "Mark Basham"]
__contact__ = "svensson@esrf.eu"
__license__ = "LGPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"

import logging, sys, traceback, os
from EDThreading import Semaphore
from EDObject import EDObject


class EDLoggingPyLogging(EDObject):
    """
    This class is meant to be used for all logging
    purposes in the EDNA framework.
    """
    __semaphoreLogging = Semaphore()
    __dictLoggers = {}
    __logLevel = logging.INFO
    __bInitisalised = False

    UNIT_TEST_LEVEL = 25
    UNIT_TEST_NAME = "UNIT_TEST"

    ASSERT_LEVEL = 55
    ASSERT_NAME = "ASSERT"


    def __init__(self, _strName=None):
        EDObject.__init__(self)
        if _strName is None:
            self.__loggingId = self.getClassName()
        else:
            self.__loggingId = _strName
        with EDLoggingPyLogging.__semaphoreLogging:
            if not EDLoggingPyLogging.__bInitisalised:
                logging.basicConfig(level=EDLoggingPyLogging.__logLevel, stream=sys.stdout)
                logging.addLevelName(EDLoggingPyLogging.UNIT_TEST_LEVEL, EDLoggingPyLogging.UNIT_TEST_NAME)
                logging.addLevelName(EDLoggingPyLogging.ASSERT_LEVEL, EDLoggingPyLogging.ASSERT_NAME)
                EDLoggingPyLogging.__bInitisalised = True
            if not self.__loggingId in EDLoggingPyLogging.__dictLoggers:
                self.logger = logging.getLogger(self.__loggingId)
                self.logger.setLevel(EDLoggingPyLogging.__logLevel)
                EDLoggingPyLogging.__dictLoggers[self.__loggingId] = self.logger
            else:
                self.logger = EDLoggingPyLogging.__dictLoggers[self.__loggingId]
        self.__bIsTest = False
        self.__bIsVerboseDebug = False
        self.__strLogFileName = None
        self.__bIsLogFile = False


    def setLogLevel(self, _logLevel):
        self.logger.setLevel(_logLevel)


    def setAllLogLevels(self, _logLevel):
        with EDLoggingPyLogging.__semaphoreLogging:
            EDLoggingPyLogging.__logLevel = _logLevel
            for logger in EDLoggingPyLogging.__dictLoggers.values():
                logger.setLevel(_logLevel)


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
        self.setAllLogLevels(logging.INFO)


    def setVerboseOff(self):
        """
        This method turns off verbose logging to standard output (stdout)
        """
        self.setAllLogLevels(max([i for i in logging._levelNames if isinstance(i, int)]) + 1)


    def setVerboseDebugOn(self):
        """
        This method turns on debug messages to standard output and log file
        """
        self.__bIsVerboseDebug = True
        self.setAllLogLevels(logging.DEBUG)


    def setVerboseDebugOff(self):
        """
        This method turns off debug messages to standard output and log file
        """
        self.__bIsVerboseDebug = False
        self.setAllLogLevels(logging.INFO)


    def isVerboseDebug(self):
        """
        This method returns the current status of debugging
        
        @return: if debug output to standard output and log file is enabled.
        @type: boolean
        """
        return self.__bIsVerboseDebug


    def log(self, _strMessage=""):
        """
        This method writes a message only to the log file.
        
        @param _strMessage: The string to be written to the log file
        @type _strMessage: python string
        """
        self.screen(_strMessage)


    def screen(self, _strMessage=""):
        """
        This method writes a message to standard output and to the log file.
        
        @param _strMessage: The string to be written to the log file
        @type _strMessage: python string
        """
        self.logger.info(_strMessage)


    def DEBUG(self, _strDebugMessage=""):
        """
        This method writes a debug message to standard output and to the log file
        if debugging is enabled. The message will be written with the prefix [DEBUG]
        
        @param _strDebugMessage: The debug message to be written to standard output and log file
        @type _strDebugMessage: python string
        """
        self.logger.debug(_strDebugMessage)


    def unitTest(self, _strMessage=""):
        """
        This method is meant to be used by the testing framework. The message will be written 
        to standard output and the log file with the prefix [UnitTest]
        
        @param _strMessage: The message to be written to standard output and log file
        @type _strMessage: python string
        """
        self.logger.log(EDLoggingPyLogging.UNIT_TEST_LEVEL, _strMessage)


    def ERROR(self, _strMessage=""):
        """
        This method writes a message to standard error and the log file with the prefix [ERROR].
        
        @param _strMessage: The error message to be written to standard output and log file
        @type _strMessage: python string
        """
        self.logger.error(_strMessage)


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
        self.logger.warning(_strMessage)


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
        self.logger.log(EDLoggingPyLogging.ASSERT_LEVEL, _strMessage)


    def writeErrorTrace(self, _strPrefix="  "):
        """
        This method writes an error trace to standard output and the log file. The error trace has
        the same formatting as normal Python error traces.
        
        @param _strPrefix: A prefix which can be customized, e.g. the testing framework uses '  [UnitTest]'
        @type _strPrefix: python string
        """
        (exc_type, exc_value, exc_traceback) = sys.exc_info()
        pyListTrace = traceback.extract_tb(exc_traceback)
        self.logger.error(_strPrefix + "Traceback (most recent call last):\n")
        for pyListLine in pyListTrace:
            self.logger.error(_strPrefix + "  File \"%s\", line %d, in %s\n" % (pyListLine[0],
                                                                                        pyListLine[1],
                                                                                        pyListLine[2]))
            self.logger.error(_strPrefix + "    " + pyListLine[3] + os.linesep)
        strErrorMessage = traceback.format_exception_only(exc_type, exc_value)[0][:-1]
        self.logger.error(_strPrefix + strErrorMessage + os.linesep)


    def setLogFileName(self, _strLogFileName):
        """
        This method can be used for customising the file name of the log file.
        
        @param _strLogFileName: A file name for the log file.
        @type _strLogFileName: python string
        """
        self.__strLogFileName = _strLogFileName


    def setLogFileOff(self):
        """
        This method truns off output to the log file.
        """
        self.__bIsLogFile = False


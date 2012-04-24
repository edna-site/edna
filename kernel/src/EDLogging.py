#
#    Project: The EDNA Kernel
#             http://www.edna-site.org
#
#    File: "$Id: EDVerbose.py 2300 2010-10-28 12:49:04Z svensson $"
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

__authors__ = ["Olof Svensson", "Jerome Kieffer"]
__contact__ = "svensson@esrf.fr"
__license__ = "LGPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"


from EDObject import EDObject
from EDLoggingVerbose import EDLoggingVerbose
from EDLoggingPyLogging import EDLoggingPyLogging


class EDLogging(EDObject):
    """
    This class loads one of the EDNA loggers: EDLoggingVerbose, EDLoggingClass
    """


    def __init__(self, _strLoggerName="EDVerbose"):
        EDObject.__init__(self)
        if _strLoggerName == "PyLogging":
            self.edLogging = EDLoggingPyLogging()
        else:
            self.edLogging = EDLoggingVerbose()


    def setLogLevel(self, _logLevel):
        self.edLogging.setLogLevel(_logLevel)


    def setAllLogLevels(self, _logLevel):
        self.edLogging.setAllLogLevels(_logLevel)


    def setTestOn(self):
        """
        turn on the test mode: all assertions become verbose (->screen) 
        """
        self.edLogging.setTestOn()


    def setTestOff(self):
        """
        turn off the test mode: all assertions become silent (->screen) 
        """
        self.edLogging.setTestOff()


    def setVerboseOn(self):
        """
        This method turns on verbose logging to standard output (stdout)
        """
        self.edLogging.setVerboseOn()


    def setVerboseOff(self):
        """
        This method turns off verbose logging to standard output (stdout)
        """
        self.edLogging.setVerboseOff()


    def setVerboseDebugOn(self):
        """
        This method turns on debug messages to standard output and log file
        """
        self.edLogging.setVerboseDebugOn()


    def setVerboseDebugOff(self):
        """
        This method turns off debug messages to standard output and log file
        """
        self.edLogging.setVerboseDebugOff()


    def isVerboseDebug(self):
        """
        This method returns the current status of debugging
        
        @return: if debug output to standard output and log file is enabled.
        @type: boolean
        """
        return self.edLogging.isVerboseDebug()


    def log(self, _strMessage=""):
        """
        This method writes a message only to the log file.
        
        @param _strMessage: The string to be written to the log file
        @type _strMessage: python string
        """
        self.edLogging.log(_strMessage)

    def screen(self, _strMessage=""):
        """
        This method writes a message to standard output and to the log file.
        
        @param _strMessage: The string to be written to the log file
        @type _strMessage: python string
        """
        self.edLogging.screen(_strMessage)


    def DEBUG(self, _strDebugMessage=""):
        """
        This method writes a debug message to standard output and to the log file
        if debugging is enabled. The message will be written with the prefix [DEBUG]
        
        @param _strDebugMessage: The debug message to be written to standard output and log file
        @type _strDebugMessage: python string
        """
        self.edLogging.DEBUG(_strDebugMessage)


    def unitTest(self, _strMessage=""):
        """
        This method is meant to be used by the testing framework. The message will be written 
        to standard output and the log file with the prefix [UnitTest]
        
        @param _strMessage: The message to be written to standard output and log file
        @type _strMessage: python string
        """
        self.edLogging.unitTest(_strMessage)


    def ERROR(self, _strMessage=""):
        """
        This method writes a message to standard error and the log file with the prefix [ERROR].
        
        @param _strMessage: The error message to be written to standard output and log file
        @type _strMessage: python string
        """
        self.edLogging.ERROR(_strMessage)


    def error(self, _strMessage=""):
        """
        This method writes a message to standard error and the log file with the prefix [ERROR].
        
        @param _strMessage: The error message to be written to standard output and log file
        @type _strMessage: python string
        """
        self.edLogging.error(_strMessage)


    def WARNING(self, _strMessage=""):
        """
        This method writes a warning message to standard output and the log file with the prefix [Warning].
        
        @param _strMessage: The error message to be written to standard output and log file
        @type _strMessage: python string
        """
        self.edLogging.WARNING(_strMessage)



    def warning(self, _strMessage=""):
        """
        This method writes a warning message to standard output and the log file with the prefix [Warning].
        
        @param _strMessage: The error message to be written to standard output and log file
        @type _strMessage: python string
        """
        self.edLogging.warning(_strMessage)


    def ASSERT(self, _strMessage):
        """
        This method writes an assert message to standard output and the log file with the prefix [ASSERT].
        
        @param _strMessage: The error message to be written to standard output and log file
        @type _strMessage: python string
        """
        self.edLogging.ASSERT(_strMessage)

    def writeErrorTrace(self, _strPrefix="  "):
        """
        This method writes an error trace to standard output and the log file. The error trace has
        the same formatting as normal Python error traces.
        
        @param _strPrefix: A prefix which can be customized, e.g. the testing framework uses '  [UnitTest]'
        @type _strPrefix: python string
        """
        self.edLogging.writeErrorTrace(_strPrefix)


    def setLogFileName(self, _strLogFileName):
        """
        This method can be used for customising the file name of the log file.
        
        @param _strLogFileName: A file name for the log file.
        @type _strLogFileName: python string
        """
        self.edLogging.setLogFileName(_strLogFileName)


    def setLogFileOff(self):
        """
        This method truns off output to the log file.
        """
        self.edLogging.setLogFileOff()


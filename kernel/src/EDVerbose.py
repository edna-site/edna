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

__authors__ = ["Olof Svensson", "Jerome Kieffer"]
__contact__ = "svensson@esrf.fr"
__license__ = "LGPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"


from EDLogging import EDLogging


class EDVerbose(object):
    """
    This class is meant to be used statically for all logging
    purposes in the EDNA framework.
    
    All methods are thread safe.
    """
    __edLogging = EDLogging("EDVerbose")


    def setTestOn():
        """
        turn on the test mode: all assertions become verbose (->screen) 
        """
        EDVerbose.__edLogging.setTestOn()
    setTestOn = staticmethod(setTestOn)


    def setTestOff():
        """
        turn off the test mode: all assertions become silent (->screen) 
        """
        EDVerbose.__edLogging.setTestOff()
    setTestOff = staticmethod(setTestOff)


    def setVerboseOn():
        """
        This method turns on verbose logging to standard output (stdout)
        """
        EDVerbose.__edLogging.setVerboseOn()
    setVerboseOn = staticmethod(setVerboseOn)


    def setVerboseOff():
        """
        This method turns off verbose logging to standard output (stdout)
        """
        EDVerbose.__edLogging.setVerboseOff()
    setVerboseOff = staticmethod(setVerboseOff)


    def setVerboseDebugOn():
        """
        This method turns on debug messages to standard output and log file
        """
        EDVerbose.__edLogging.setVerboseDebugOn()
    setVerboseDebugOn = staticmethod(setVerboseDebugOn)


    def setVerboseDebugOff():
        """
        This method turns off debug messages to standard output and log file
        """
        EDVerbose.__edLogging.setVerboseDebugOff()
    setVerboseDebugOff = staticmethod(setVerboseDebugOff)


    def isVerboseDebug():
        """
        This method returns the current status of debugging
        
        @return: if debug output to standard output and log file is enabled.
        @type: boolean
        """
        return EDVerbose.__edLogging.isVerboseDebug()
    isVerboseDebug = staticmethod(isVerboseDebug)


    def log(_strMessage=""):
        """
        This method writes a message only to the log file.
        
        @param _strMessage: The string to be written to the log file
        @type _strMessage: python string
        """
        EDVerbose.__edLogging.log(_strMessage)
    log = staticmethod(log)


    def screen(_strMessage=""):
        """
        This method writes a message to standard output and to the log file.
        
        @param _strMessage: The string to be written to the log file
        @type _strMessage: python string
        """
        EDVerbose.__edLogging.screen(_strMessage)
    screen = staticmethod(screen)


    def DEBUG(_strDebugMessage=""):
        """
        This method writes a debug message to standard output and to the log file
        if debugging is enabled. The message will be written with the prefix [DEBUG]
        
        @param _strDebugMessage: The debug message to be written to standard output and log file
        @type _strDebugMessage: python string
        """
        EDVerbose.__edLogging.DEBUG(_strDebugMessage)
    DEBUG = staticmethod(DEBUG)


    def unitTest(_strMessage=""):
        """
        This method is meant to be used by the testing framework. The message will be written 
        to standard output and the log file with the prefix [UnitTest]
        
        @param _strMessage: The message to be written to standard output and log file
        @type _strMessage: python string
        """
        EDVerbose.__edLogging.unitTest(_strMessage)
    unitTest = staticmethod(unitTest)


    def ERROR(_strMessage=""):
        """
        This method writes a message to standard error and the log file with the prefix [ERROR].
        
        @param _strMessage: The error message to be written to standard output and log file
        @type _strMessage: python string
        """
        EDVerbose.__edLogging.ERROR(_strMessage)
    ERROR = staticmethod(ERROR)


    def error(_strMessage=""):
        """
        This method writes a message to standard error and the log file with the prefix [ERROR].
        
        @param _strMessage: The error message to be written to standard output and log file
        @type _strMessage: python string
        """
        EDVerbose.__edLogging.error(_strMessage)
    error = staticmethod(error)


    def WARNING(_strMessage=""):
        """
        This method writes a warning message to standard output and the log file with the prefix [Warning].
        
        @param _strMessage: The error message to be written to standard output and log file
        @type _strMessage: python string
        """
        EDVerbose.__edLogging.WARNING(_strMessage)
    WARNING = staticmethod(WARNING)


    def warning(_strMessage=""):
        """
        This method writes a warning message to standard output and the log file with the prefix [Warning].
        
        @param _strMessage: The error message to be written to standard output and log file
        @type _strMessage: python string
        """
        EDVerbose.__edLogging.warning(_strMessage)
    warning = staticmethod(warning)


    def ASSERT(_strMessage):
        """
        This method writes an assert message to standard output and the log file with the prefix [ASSERT].
        
        @param _strMessage: The error message to be written to standard output and log file
        @type _strMessage: python string
        """
        EDVerbose.__edLogging.ASSERT(_strMessage)
    ASSERT = staticmethod(ASSERT)


    def writeErrorTrace(_strPrefix="  "):
        """
        This method writes an error trace to standard output and the log file. The error trace has
        the same formatting as normal Python error traces.
        
        @param _strPrefix: A prefix which can be customized, e.g. the testing framework uses '  [UnitTest]'
        @type _strPrefix: python string
        """
        EDVerbose.__edLogging.writeErrorTrace(_strPrefix)
    writeErrorTrace = staticmethod(writeErrorTrace)


    def setLogFileName(_strLogFileName):
        """
        This method can be used for customising the file name of the log file.
        
        @param _strLogFileName: A file name for the log file.
        @type _strLogFileName: python string
        """
        EDVerbose.__edLogging.setLogFileName(_strLogFileName)
    setLogFileName = staticmethod(setLogFileName)


    def setLogFileOff():
        """
        This method truns off output to the log file.
        """
        EDVerbose.__edLogging.setLogFileOff()
    setLogFileOff = staticmethod(setLogFileOff)

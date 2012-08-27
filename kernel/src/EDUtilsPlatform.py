# -*- coding: utf8 -*-
#
#    Project: The EDNA Kernel
#             http://www.edna-site.org
#
#    File: "$Id: EDUtilsPath.py 1484 2010-05-05 07:08:21Z svensson $"
#
#    Copyright (C) 2008-2010 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal authors: Jérôme Kieffer (jerome.kieffer@esrf.fr)
# 
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
__authors__ = [ "Jérôme Kieffer" ]
__contact__ = "jerome.kieffer@esrf.fr"
__license__ = "LGPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"


import sys, os, math, distutils.util, signal, subprocess
from EDThreading import Semaphore
from EDVerbose import EDVerbose


class classproperty(property):
    def __get__(self, obj, type_):
        return self.fget.__get__(None, type_)()
    def __set__(self, obj, value):
        cls = type(obj)
        return self.fset.__get__(None, cls)(value)


class EDUtilsPlatform(object):
    """
    Static class for guessing: platform specific stuff.
    
    """
    __semaphore = Semaphore()
    __semaphore.acquire()
    __strCmdSep = None
    __strCmdEnv = None
    __strEscapedLineSep = None
    __strLineSep = os.linesep
    __strSep = os.sep
    __strAltSep = os.altsep
    __strExtSep = os.extsep
    __strPathSep = os.pathsep
    __strName = os.name
    __strStartScript = None
    __PythonPlatformSize = int(round(math.log(sys.maxint + 1) / math.log(2) + 1))

    __SystemPlatform = distutils.util.get_platform()
    if __PythonPlatformSize == 32 and __SystemPlatform.endswith("x86_64"):
        __PythonPlatform = __SystemPlatform[:-6] + "i386"
    else:
        __PythonPlatform = __SystemPlatform
    __PythonArchitecture = "lib.%s-%i.%i" % (__PythonPlatform, sys.version_info[0], sys.version_info[1])
    if sys.maxunicode == 65535:
        __PythonArchitecture += "-ucs2"
    __SystemArchitecture = "lib.%s-%i.%i" % (__SystemPlatform, sys.version_info[0], sys.version_info[1])

    if os.name == "java": # Then we are running under Jython !
        from java.lang import System as javasystem
        if javasystem.getProperty("os.name").startswith("Windows"):
            __strName = "nt"
        else:
            __strName = "posix"

    if  __strName == "nt":
        __strCmdSep = "&"
        __strCmdEnv = "set"
        __strEscapedSep = "/"
        __strEscapedLineSep = "\\r\\n"
        __strStartScript = "@ECHO OFF"
    elif __strName == "posix":
        __strCmdSep = ";"
        __strCmdEnv = "env"
        __strEscapedSep = "\\\\"
        __strEscapedLineSep = "\\n"
        __strStartScript = "#!%s" % sys.executable
    __semaphore.release()



    @classmethod
    def getArchitecture(cls):
        """
        Returns the name of the architecture including the CPU arch and the version of python for the actual running python
        (i.e. can be i386 on a x86_64 computer) 
        @return: lib-$OS-$arch-$PyVersion
        @rtype: python string
        """
        return cls.__PythonArchitecture
    architecture = classproperty(getArchitecture)


    @classmethod
    def getSystemArchitecture(cls):
        """
        Returns the name of the architecture including the CPU arch and the version of python for the actual operating system
        @return: lib-$OS-$arch-$PyVersion
        @rtype: python string
        """
        return cls.__SystemArchitecture
    systemArchitecture = classproperty(getSystemArchitecture)


    @classmethod
    def getName(cls):
        """
        Returns the name of the architecture
        @return: os.name like architecture (posix, nt, ... but never java even under jython)
        @rtype: python string
        """
        return cls.__strName
    name = classproperty(getName)


    @classmethod
    def getCmdSep(cls):
        """
        Returns the Command separator like 
        - Under Unix: cmd1;cmd2
        - Under Windows cmd1 & cmd2 
        @return: "&" or ";" depending on the architecture
        @rtype: python string
        """
        return cls.__strCmdSep
    cmdSep = classproperty(getCmdSep)


    @classmethod
    def getCmdEnv(cls):
        """
        @return: "env" or "set" to print the environment under the current operating system 
        """
        return cls.__strCmdEnv
    cmdEnv = classproperty(getCmdEnv)


    @classmethod
    def getEscapedSep(cls):
        """
        return os.sep with "\" escaped
        """
        return cls.__strEscapedSep
    escapedSep = classproperty(getEscapedSep)


    @classmethod
    def getEscapedLineSep(cls):
        """
        return os.linesep with "\" escaped
        """
        return cls.__strEscapedLineSep
    escapedLinesep = classproperty(getEscapedLineSep)


    @classmethod
    def getLineSep(cls):
        """
        @return os.linesep
        """
        return cls.__strLineSep
    linesep = classproperty(getLineSep)


    @classmethod
    def getSep(cls):
        """
        @return: os.sep
        """
        return cls.__strSep
    sep = classproperty(getSep)


    @classmethod
    def getStartScript(cls):
        """
        @return: header for writing scripts under the current the archtecture (#!/usr/bin/python under linux)
        """
        return cls.__strStartScript
    startScript = classproperty(getStartScript)


    @classmethod
    def getSize(cls):
        """
        @return: the size of the environment, probably 32 or 64 bits
        """
        return cls.__PythonPlatformSize
    size = classproperty(getSize)

    @classmethod
    def getSystemPlatform(cls):
        """
        @return: linux-x86_64, if python 32bits is running under amd64 OS. 
        """
        return cls.__SystemPlatform
    systemPlatform = classproperty(getSystemPlatform)


    @classmethod
    def getPythonPlatform(cls):
        """
        @return: linux-i386, if python 32bits is running under amd64 OS. 
        """
        return cls.__PythonPlatform
    pythonPlatform = classproperty(getPythonPlatform)


    @classmethod
    def getAltSep(cls):
        """
        @return: os.altsep
        """
        return cls.__strAltSep
    altsep = classproperty(getAltSep)


    @classmethod
    def getExtSep(cls):
        """
        @return: "." as extension separator
        """
        return cls.__strExtSep
    extsep = classproperty(getExtSep)


    @classmethod
    def getPathSep(cls):
        """
        same as os.pathsep
        @return "/" under linux and "\" under windows. 
        """
        return cls.__strPathSep
    pathsep = classproperty(getPathSep)

    @classmethod
    def escape(cls, _string):
        """
        escape \ (i.e. "\\") under windows as \\ (i.e. "\\\\") 
        @return escaped string suitable for metaprogramming 
        """
        return  _string.replace("\\", "\\\\")


    @classmethod
    def Popen(cls, *args, **kwargs):
        """
        implementation of a platform independent subprocess.Popen method
        
        @return: subporcess.Popen instance.
        """
        if os.name == "posix": #python under unix
            kwargs["preexec_fn"] = os.setsid
        return subprocess.Popen(*args, **kwargs)




    @classmethod
    def kill(cls, _iPid):
        """
        implementation of a platform independent kill method 
        
        @param _iPid: process ID
        @type _iPid: integer
        """
        EDVerbose.log("EDUtilsPlatorm.kill called on PID: %s" % _iPid)
        if os.name == "posix": #python under unix
            os.killpg(_iPid, signal.SIGKILL)
        elif cls.architecture == "posix": #jython running under unix
            os.kill(_iPid, signal.SIGKILL)
        else: #windows, ... Nota: this only works from python2.7 under windows !
            EDVerbose.WARNING("Kill Called to PID= %s with signal %s" % (_iPid, signal.SIGTERM))
            os.kill(_iPid, signal.SIGTERM)

# -*- coding: utf8 -*-
#
#    Project: PROJECT
#             http://www.edna-site.org
#
#    File: "$Id: EDParallelExecute.py 1397 2010-04-22 06:40:16Z svensson $"
#
#    Copyright (C) European Synchrotron Radiation Facility, Grenoble, France
#
#    Principal author:       Jérôme Kieffer (Jerome.Kieffer@ESRF.eu)
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

"""

Some useful static methods dealing with parallel programming and the number of CPU detection 

"""

__author__ = "Jerome Kieffer"
__contact__ = "Jerome.Kieffer@ESRF.eu"
__license__ = "LGPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"

import threading, os, sys, re, subprocess
from EDVerbose import EDVerbose


class EDUtilsParallel:
    """ 
    A class helping to make a multi-threaded application. 
    """
    __iActualNbCPU = None
    __semaphore = threading.Semaphore()
    __semaphoreInit = threading.Semaphore()
    __semaphoreNbThreads = None
    __iNbThreads = None


    @staticmethod
    def __detectNumberOfCPUs():
        """
        detect the actual number of CPUs and stores it in a class variable 
        """
        EDUtilsParallel.__semaphore.acquire()
        if EDUtilsParallel.__iActualNbCPU is not None:
            return
        iNbCPU = None
        #The best way: using python 2.6 or later
        try:
            import multiprocessing
            iNbCPU = multiprocessing.cpu_count()

        except (ImportError, NotImplementedError):
            iNbCPU = None

        # POSIX
        if iNbCPU is None:
            try:
                iNbCPU = int(os.sysconf('SC_NPROCESSORS_ONLN'))
                if iNbCPU <= 0:
                    iNbCPU = None
            except (AttributeError, ValueError):
                iNbCPU = None

        # Windows
        if iNbCPU is None:
            try:
                iNbCPU = int(os.environ['NUMBER_OF_PROCESSORS'])
                if iNbCPU <= 0:
                    iNbCPU = None
            except (KeyError, ValueError):
                iNbCPU = None

        # jython
        if iNbCPU is None:
            try:
                from java.lang import Runtime
                runtime = Runtime.getRuntime()
                iNbCPU = runtime.availableProcessors()
                if iNbCPU <= 0:
                    iNbCPU = None
            except ImportError:
                iNbCPU = None

        # BSD
        if iNbCPU is None:
            try:
                sysctl = subprocess.Popen(['sysctl', '-n', 'hw.ncpu'], stdout=subprocess.PIPE)
                scStdout = sysctl.communicate()[0]
                iNbCPU = int(scStdout)
                if iNbCPU <= 0:
                    iNbCPU = None
            except (OSError, ValueError):
                iNbCPU = None

        # Linux
        if iNbCPU is None:
            try:
                iNbCPU = open('/proc/cpuinfo').read().count('processor\t:')
                if iNbCPU <= 0:
                    iNbCPU = None
            except IOError:
                iNbCPU = None

        # Solaris
        if iNbCPU is None:
            try:
                pseudoDevices = os.listdir('/devices/pseudo/')
                expr = re.compile('^cpuid@[0-9]+$')
                iNbCPU = 0
                for pd in pseudoDevices:
                    if expr.match(pd) != None:
                        iNbCPU += 1
                if iNbCPU <= 0:
                    iNbCPU = None
            except OSError:
                iNbCPU = None

        # Other UNIXes (heuristic)
        if iNbCPU is None:
            try:
                try:
                    dmesg = open('/var/run/dmesg.boot').read()
                except IOError:
                    dmesgProcess = subprocess.Popen(['dmesg'], stdout=subprocess.PIPE)
                    dmesg = dmesgProcess.communicate()[0]
                iNbCPU = 0
                while '\ncpu' + str(iNbCPU) + ':' in dmesg:
                    iNbCPU += 1
                if iNbCPU <= 0:
                    iNbCPU = None
            except OSError:
                iNbCPU = None

        #if nothing else works ...
        if iNbCPU is None:
            iNbCPU = 1

        EDUtilsParallel.__iActualNbCPU = iNbCPU
        EDUtilsParallel.__semaphore.release()


    @staticmethod
    def detectNumberOfCPUs(_iMaxCPU=sys.maxint, _bForce=False):
        """
        class method :
        Detects the number of CPUs on a system. Cribbed from pp.
        found : http://www.boduch.ca/2009/06/python-cpus.html
        
        @param _iMaxCPU: the maximum number of CPUs allowed 
        @type _iMaxCPU: integer
        @param  _bForce: force the number of CPUs for debugging
        @type _bForce: boolean
        @return: the number of CPUs
        @rtype: integer
        """
        if not isinstance(_iMaxCPU, int):
            _iMaxCPU = sys.maxint
        else:
            _iMaxCPU = max(1, _iMaxCPU)

        if isinstance(_bForce, bool):
            if _bForce:
                return _iMaxCPU

        if EDUtilsParallel.__iActualNbCPU is None:
            EDUtilsParallel.__detectNumberOfCPUs()
        iNbCPU = EDUtilsParallel.__iActualNbCPU
        if iNbCPU < 1:
            return 1
        elif iNbCPU > _iMaxCPU :
            return _iMaxCPU
        else:
            return iNbCPU


    @staticmethod
    def initializeNbThread(_iNbThread=None):
        """
        Class method:
        Initialises a semaphore with the right number of threads
        @param _iNbThread: the maximum number of threads concurrently running and CPU intensive
        @type _iNbThread: integer
        """
        EDUtilsParallel.__semaphoreInit.acquire()
        if EDUtilsParallel.__semaphoreNbThreads is None:
            if _iNbThread is None:
                _iNbThread = EDUtilsParallel.detectNumberOfCPUs()
            EDVerbose.DEBUG("Initializing EDUtilsParallel semaphoreNbThreads to %i" % _iNbThread)
            EDUtilsParallel.__iNbThreads = _iNbThread
            EDUtilsParallel.__semaphoreNbThreads = threading.Semaphore(_iNbThread)
        else:
            if EDUtilsParallel.__iNbThreads != _iNbThread:
                EDVerbose.WARNING("EDUtilsParallel.__semaphoreNbThreads was already initialized to %i, not changing to %i" % (EDUtilsParallel.__iNbThreads, _iNbThread))
        EDUtilsParallel.__semaphoreInit.release()


    @staticmethod
    def uninitializeNbThread():
        """
        For testing purpose: un-initialize the semaphore controlling the number of execPlugin running at once  
        """
        if EDUtilsParallel.__semaphoreNbThreads is not None:
            EDVerbose.DEBUG("resetting the semaphore concerning the number of threads.")
            EDUtilsParallel.__semaphoreNbThreads = None


    @staticmethod
    def getSemaphoreValue():
        """
        Class method:
        getter for the current value of the semaphore counting the CPU-active threads
        
        @return: value of the semaphore (or None if not initialized) 
        @rtype: int
        """
        if EDUtilsParallel.__semaphoreNbThreads is not None:
            return EDUtilsParallel.__semaphoreNbThreads._Semaphore__value
        else:
            return None


    @staticmethod
    def getNbRunning():
        """
        Class method:
        getter for the number of CPU-active threads running
    
        @return: the number of CPU-active threads runnings
        @rtype: integer
        """
        if EDUtilsParallel.__semaphoreNbThreads is not None:
            return EDUtilsParallel.__iNbThreads - EDUtilsParallel.__semaphoreNbThreads._Semaphore__value
        else:
            return None


    @staticmethod
    def semaphoreNbThreadsAcquire():
        """
        Class method:
        Method to acquire the semaphore that controls the number of threads running concurrently
        """
        if EDUtilsParallel.__semaphoreNbThreads is not None:
            EDUtilsParallel.__semaphoreNbThreads.acquire()
        else:
            EDVerbose.DEBUG("EDUtilsParallel: Unable to acquire an uninitialized semaphore (NbCPU).")


    @staticmethod
    def semaphoreNbThreadsRelease():
        """
        Class method:
        Method to release the semaphore that controls the number of threads running concurrently
        """
        if EDUtilsParallel.__semaphoreNbThreads is not None:
            if EDUtilsParallel.__semaphoreNbThreads._Semaphore__value < EDUtilsParallel.__iNbThreads:
                EDUtilsParallel.__semaphoreNbThreads.release()
        else:
            EDVerbose.DEBUG("EDUtilsParallel: Unable to release an uninitialized semaphore (NbCPU).")


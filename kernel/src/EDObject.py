# coding: utf8
#
#    Project: The EDNA Kernel
#             http://www.edna-site.org
#
#    File: "$Id: EDImportLib.py 1453 2010-04-28 16:20:46Z svensson $"
#
#    Copyright (C) 2010-2010 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal authors: 
#                       Olof Svensson (svensson@esrf.fr) 
#                       Jérôme Kieffer (jerome.kieffer@esrf.fr)
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
EDObject is the core of all EDNA objects, 
it offers some simple but efficient synchronization scheme based on Semaphores 
it offers timing facilities (uninitialized by default) 
"""

__authors__ = ["Olof Svensson", "Jérôme Kieffer"]
__contact__ = "svensson@esrf.eu"
__license__ = "LGPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"


import time
from EDThreading import Semaphore

class EDObject(object):
    """
    Virtual base class for all EDNA Objects (classes).
    It offers some synchronization and locking capabilities to make the code thread safe.
    """
    __semaphoreId = Semaphore()
    __iId_class = 0

    def __init__(self):
        """
        Constructor of the main pure virtual class.
        This constructor implements:
        - the creation of the semaphore
        - definition of timer object (uninitialized as potentially not used)
        """
        object.__init__(self)
        with self.__class__.__semaphoreId:
            self.__class__.__iId_class += 1
            self.__iId = self.__class__.__iId_class
        self.__semaphore = Semaphore()
        self.__fTimeInit = None
        self.__fTimeEnd = None
        self.__classname = None


    def getId(self):
        return self.__iId


    def getClassName(self):
        """
        Retrieves the name of the class
        @return: the name of the class 
        @rtype: string 
        """
        return self.__class__.__name__


    def synchronizeOn(self):
        """
        This method must be used in together with the method synchronizeOff().
        This method makes the code threadsafe till the method synchronizeOff
        is called.
        """
        self.__semaphore.acquire()


    def synchronizeOff(self):
        """
        This method must be used in together with the method synchronizeOn().
        """
        self.__semaphore.release()


    def getSemaphoreValue(self):
        """
        This method should only be used for debugging purpose...
        @return: the "internal" value of the semaphore
        @rtype: integer
        """
        iValue = self.__semaphore._Semaphore__value
        #EDVerbose.WARNING("DEBUG INFO: The value of semaphore for instance of class %s with hash %s is %i" % (self.getClassName(), hash(self), iValue))
        return iValue

    def locked(self):
        return self.__semaphore


    def setTimeInit(self):
        """
        Initializes the timer for the object
        """
        if self.__fTimeInit is None:
            self.__fTimeInit = time.time()




    def getTimeInit(self):
        """
        Retrieves the time of initialization
        @return: number of seconds since epoch
        @rtype: float  
        """
        return self.__fTimeInit


    def setTimeEnd(self):
        """
        Set the end of calculation time for the given object
        """
        if self.__fTimeEnd is None:
            self.__fTimeEnd = time.time()


    def getTimeEnd(self):
        """
        Retrieves the time of end of task
        @return: number of seconds since epoch
        @rtype: float  
        """
        return self.__fTimeEnd

    def getRunTime(self):
        """
        @returns: the RunTime for the given object
        @rtype: float
        """
        fRetrunRunTime = 0.0
        if self.__fTimeInit is not None:
            if self.__fTimeEnd is None:
                fRetrunRunTime = time.time() - self.__fTimeInit
            else:
                fRetrunRunTime = self.__fTimeEnd - self.__fTimeInit
        return fRetrunRunTime



#
#    Project: The EDNA Kernel
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2008-2010 European Synchrotron Radiation Facility
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


__authors__ = [ "Olof Svensson" ]
__contact__ = "svensson@esrf.fr"
__license__ = "LGPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"

"""
This class is used for creating a "cluster" of plugins that are launched
in parallel and the synchronized.
"""


import threading

from EDAction import EDAction

from EDUtilsParallel import EDUtilsParallel

class EDActionCluster(EDAction):
    """
    This class is used for creating a "cluster" of actions (e.g. plugins) that are launched
    in parallel and then synchronized.
    """


    def __init__(self, _iNoThreads=None):
        """
        Initalises the action cluster. The max number of threads to be used can be forced,
        if omitted the number of processors number of threads  
        @param _iNoThreads: max number of threads to be used
        @type  _iNoThreads: integer        
        """
        EDAction.__init__(self)
        self.__iNoThreads = _iNoThreads
        self.__semaphoreActionCluster = None
        self.__lActions = []


    def process(self, _edPlugin=None):
        """
        Executes the action cluster. This method will return only when
        all actions have finished.
        """
        self.DEBUG("EDActionCluster.process")
        if (not self.__iNoThreads):
            self.__iNoThreads = EDUtilsParallel.detectNumberOfCPUs()
        self.__semaphoreActionCluster = threading.Semaphore(self.__iNoThreads)
        for edAction in self.__lActions:
            edAction.connectSUCCESS(self.__semaphoreRelease)
            edAction.connectFAILURE(self.__setActionClusterFailure)
            edAction.connectFAILURE(self.__semaphoreRelease)
            self.DEBUG("EDActionCluster.process : Starting action %s" % edAction.getClassName())
            self.__semaphoreActionCluster.acquire()
            edAction.execute()
        # Wait for all threads to finish
        for edAction in self.__lActions:
            edAction.join()



    def __semaphoreRelease(self, _edAction=None):
        """
        This private method is called if the edAction executed as part of the action
        cluster is a success. It will release one thread from the semaphore of the action
        so that a new thread can be started.
        """
        self.DEBUG("EDActionCluster.__semaphoreRelease : action %s ended." % _edAction.getClassName())
        self.__semaphoreActionCluster.release()


    def __setActionClusterFailure(self, _edAction=None):
        """
        This is a private method that sets the EDActioCluster instance to failure if one
        of the actions ends in failure.
        """
        self.DEBUG("EDActionCluster.__setActionClusterFailure called from action %s" % _edAction.getClassName())
        self.setFailure()
        

    def addAction(self, _edAction):
        """
        This method adds an action (e.g. plugin) to the list of actions to be executed in parallel.
        @param _edAction: an actiond, e.g. a plugin
        @type  _edAction: EDAction
        """
        self.__lActions.append(_edAction)


    def setClusterSize(self, _iNoThreads):
        """
        This method forces the number of threads to be used of the action cluster.
        @param _iNoThreads: max number of threads to be used
        @type  _iNoThreads: integer        
        """
        self.__iNoThreads = _iNoThreads

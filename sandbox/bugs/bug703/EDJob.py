#!/usr/bin/env python
# -*- coding: utf8 -*-
#
#    Project: EDNA-Kernel
#             http://www.edna-site.org
#
#    File: "$Id: EDParallelExecute.py 1990 2010-08-26 09:10:15Z svensson $"
#
#    Copyright (C) European Synchrotron Radiation Facility, Grenoble, France
#
#    Principal author:       Jérôme Kieffer (Jerome.Kieffer@ESRF.eu)
#
#    Contributing author:    Olof Svensson (svensson@esrf.fr)
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
Create a module called EDJob
* Most of what was done up to 09-2010 in EDParallelExecute should be done here
* Each instance will be a job
* Constructor takes a plugin name
* Each instance will have taking an "setDataInput" method getting an XMLin
* Each instance will gave a "getDataOutput" method, this could be a "join", waiting for the job to finish
* Each instance will have a "execute" method  and  returning a JobId 
* Each instance will have a "setCallBack" method  that stores the name of the external callback 


* provide status of a job
* keep track of all plugin status
* leave the time to plugin to initialize
* static class retrieve job-instance, status, small-log ...
* prevent multiple run of a single job ?
* does not manage workload of the computer, should be managed at the ExecPlugin level

Used for the tango binding, EDParallelExecute ...

== class variables ==
dictPluginStatus[pluginName] = ["uninitialized"|"running"|"executed"| "failed"]
dictJobs [JobId] = EDJob.Instance

== static methods ==
getJob(JobId)
"""

__authors__ = ["Jérôme Kieffer", "Olof Svensson"]
__contact__ = "Jerome.Kieffer@ESRF.eu"
__license__ = "LGPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"


import threading, time, os
from EDVerbose              import EDVerbose
from EDFactoryPluginStatic  import EDFactoryPluginStatic
from EDFactoryPlugin        import EDFactoryPlugin
from EDObject               import EDObject
from EDSlot                 import EDSlot
from EDPluginWrapperForJobScheduler import EDPluginWrapperForJobScheduler

#asizeof does not work with Jython
if  os.name == "java":
    asizeof = None
else:
    asizeof = EDFactoryPluginStatic.loadModule("asizeof")

class EDJob(EDObject):

    PLUGIN_STATE_UNITIALIZED = "uninitialized"
    PLUGIN_STATE_RUNNING = "running"
    PLUGIN_STATE_SUCCESS = "success"
    PLUGIN_STATE_FAILURE = "failure"

    __edFactoryPlugin = EDFactoryPlugin()
    __dictJobs = {}
    __semaphore = threading.Semaphore()
    __dictPluginLastId = {}
    __fStartTime = time.time()

    def __init__(self, _strPluginName):
        """
        Constructor of the class
        
        @param strPluginName: name of the plugin 
        @type strPluginName: string
        """
        EDObject.__init__(self)
        self.__strPluginName = _strPluginName
        self.__edPlugin = None
        self.__edSlotCallBack = EDSlot()
        self.__edSlotSUCCESS = EDSlot()
        self.__edSlotFAILURE = EDSlot()
        self.__bXmlInputSet = False
        self.__status = None
#        self.__edPlugin = EDJob.__edFactoryPlugin.loadPlugin(self.__strPluginName)
        self.__edPlugin = EDPluginWrapperForJobScheduler(self.__strPluginName)
        EDJob.__semaphore.acquire()
#        Create the JobID
        if not self.__strPluginName in EDJob.__dictPluginLastId:
            EDJob.__dictPluginLastId[_strPluginName] = 0
        else:
            EDJob.__dictPluginLastId[_strPluginName] += 1
        self.__jobId = "%s-%i" % (self.__strPluginName, EDJob.__dictPluginLastId[_strPluginName])
        EDJob.__dictJobs[self.__jobId] = self
        EDJob.__semaphore.release()
        if (self.__edPlugin is None):
            EDVerbose.WARNING("Instantiation of plugin %s failed!!!" % _strPluginName)
        else:
            self.__status = EDJob.PLUGIN_STATE_UNITIALIZED


    def setDataInput(self, _oDataInput, _strDataInputKey=None):
        """
        Sets the job (plugin) input data.
        
        @param: _oDataInput: could be either an String XML or an XSData object.
        @param _strDataInputKey: the key of an input data dictionnary
        
        The input data is stored in a dictionary with the key _strDataInputKey.
        If the key is not provided a default key is used.

        If not data input class is defined for the key an exception is raised.
        
        If the key is not the default key, the data object is added to a list which 
        might contain already stored object(s).
        
        If _oDataInput is None the list corresponding to a keyword is deleted.
        """

        if _oDataInput in ["", None]:
            self.__bXmlInputSet = False
            return
        self.synchronizeOn()
        if (self.__edPlugin is not None):
            self.__edPlugin.setDataInput(_oDataInput, _strDataInputKey)
            self.__bXmlInputSet = True
        else:
            EDVerbose.WARNING("Setting DataInput for uninstanciated plugin %s." % self.__strPluginName)
        self.synchronizeOff()


    def getDataInput(self, _strDataInputKey=None):
        """
        Returns the Plugin Input Data for a particular key.
        If the key is not provided a default key is used.
        """
        if (self.__edPlugin is not None):
            return self.__edPlugin.getDataInput(_strDataInputKey)
        else:
            EDVerbose.WARNING("Getting DataInput for uninstanciated plugin %s." % self.__strPluginName)


    def getDataOutput(self, _strDataOutputKey=None):
        """
        Returns the Plugin Output Data
        """
        if (self.__edPlugin is not None):
            return self.__edPlugin.getDataOutput(_strDataOutputKey)
        else:
            EDVerbose.WARNING("Getting DataOutput for uninstanciated plugin %s." % self.__strPluginName)


    def execute(self):
        """
        Launch the EDNA plugin
        @return: JobId
        @rtype: string
        """
        returnId = None
        if not self.__bXmlInputSet:
            EDVerbose.WARNING("Not executing job %s as input is empty" % self.__jobId)

        if (self.__edPlugin is not None):
            self.synchronizeOn()
            self.__status = EDJob.PLUGIN_STATE_RUNNING
            self.__edPlugin.connectSUCCESS(self.successPluginExecution)
            self.__edPlugin.connectFAILURE(self.failurePluginExecution)
            self.__edPlugin.execute()
            returnId = self.__jobId
            self.synchronizeOff()

        else:
            EDVerbose.WARNING("Trying to run a plugin that does not exist: %s " % self.__strPluginName)

        return returnId


    def synchronize(self):
        """
        Synchronize the execution of the job with the calling thread.
        """
        self.__edPlugin.synchronize()


    def successPluginExecution(self, _edObject=None):
        """
        Method called when the execution of the plugin succeeds 
        """
        self.synchronizeOn()
        self.__status = EDJob.PLUGIN_STATE_SUCCESS
        EDVerbose.screen("Plugin %s execution ended with success" % self.__jobId)
        self.synchronizeOff()
        try:
            self.__edSlotSUCCESS.call(self.__jobId)
        except Exception:
            EDVerbose.ERROR("Error in execution of Success call-back for %s" % self.__jobId)
            EDVerbose.writeErrorTrace()
        try:
            self.__edSlotCallBack.call(self.__jobId)
        except Exception:
            EDVerbose.ERROR("Error in execution of Common call-back (after success) for %s" % self.__jobId)
            EDVerbose.writeErrorTrace()


    def failurePluginExecution(self, _edObject=None):
        """
        Method called when the execution of the plugin failed 
        """
        self.synchronizeOn()
        self.__status = EDJob.PLUGIN_STATE_FAILURE
        EDVerbose.screen("Plugin %s execution ended with failure" % self.__jobId)
        self.synchronizeOff()
        try:
            self.__edSlotFAILURE.call(self.__jobId)
        except Exception:
            EDVerbose.ERROR("Error in execution of Failure call-back for %s" % self.__jobId)
            EDVerbose.writeErrorTrace()
        try:
            self.__edSlotCallBack.call(self.__jobId)
        except Exception:
            EDVerbose.ERROR("Error in execution of Common call-back (after failure) for %s" % self.__jobId)
            EDVerbose.writeErrorTrace()


    def connectSUCCESS(self, _oMethod):
        self.synchronizeOn()
        if (_oMethod != None):
            self.__edSlotSUCCESS.connect(_oMethod)
        self.synchronizeOff()


    def connectFAILURE(self, _oMethod):
        self.synchronizeOn()
        if (_oMethod != None):
            self.__edSlotFAILURE.connect(_oMethod)
        self.synchronizeOff()


    def connectCallBack(self, _oMethod):
        self.synchronizeOn()
        if (_oMethod != None):
            self.__edSlotCallBack.connect(_oMethod)
        self.synchronizeOff()


    def getJobId(self):
        """
        @return: JobId i.e. EDPluginName-Number
        @rtype: string
        """
        return self.__jobId


    def getPluginName(self):
        """
        @return: Name of the plugin
        @rtype: string
        """
        return self.__strPluginName


    def getPlugin(self):
        """
        @return: the plugin (instance)
        @rtype: python object
        """
        return self.__edPlugin


    def getStatus(self):
        """
        @return: status of the Job
        @rtype: string
        """
        return self.__status


    def getMemSize(self):
        """
        try to guess the size in memory of a job
        @return: expected size in memory 
        """
        if asizeof is not None:
            return asizeof.asizeof(self)


    @staticmethod
    def getStatusFromID(jobId):
        """
        Retrieve the job (hence the plugin) status
        
        @param jobId: the Job identification number
        @type jobId: string
        @return: the EDJob status 
        @rtype: string 
        """
        if jobId in EDJob.__dictJobs:
            return EDJob.__dictJobs[jobId].getStatus()
        else:
            EDVerbose.WARNING("Unable to retrieve such EDJob: %s" % jobId)


    @staticmethod
    def getJobFromID(jobId):
        """
        Retrieve the job (hence the plugin)
        
        @param jobId: the Job identification number
        @type jobId: string
        @return: the "EDJob instance", which contains the plugin (__edPlugin) and the status
        @rtype: a Python object. 
        """
        if jobId in EDJob.__dictJobs:
            return EDJob.__dictJobs[jobId]
        else:
            EDVerbose.WARNING("Unable to retrieve such EDJob: %s" % jobId)



    @staticmethod
    def getMemoryFootprint():
        if asizeof is not None:
            return asizeof.asizesof(EDJob.__dictJobs)


    @staticmethod
    def stats():
        """
        retrieve some statistics
        """
        output = []
        fExecTime = time.time() - EDJob.__fStartTime
        keys = EDJob.__dictJobs.keys()
        for key in keys :
            num = int(key.split("-", 1)[1])
            job = EDJob.__dictJobs[key]
            output.append([num, job.getPluginName(), job.getStatus(), job.getPlugin().getRunTime(), job.getMemSize()])
        output.sort()
        iNbJob = max(1, len(output))
        EDVerbose.screen("%s\t|\t%s\t\t\t|\t%s\t|\t%s\t\t|\t%s" % ("id", "EDPluginName", "status", "runtime", "memory"))
        fWall = 0.0
        fSumProd = 0.0
        fSumX = 0.0
        fSumX2 = 0.0
        for oneJob in output:
            fWall += oneJob[3]
            fSumX += oneJob[0]
            fSumX2 += oneJob[0] * oneJob[0]
            fSumProd += oneJob[0] * oneJob[3]
            EDVerbose.screen("%s\t|\t%s\t|\t%s\t|\t%9.3f\t|\t%s" % tuple(oneJob))
        EDVerbose.screen("_" * 90)
        EDVerbose.screen("Total execution time (Wall): %.3fs, Execution time: %.3fs. SpeedUp: %.3f" % (fWall, fExecTime, fWall / fExecTime))
        EDVerbose.screen("Average execution time (Wall/N): %.3fs, Average throughput: %.3fs" % (fWall / iNbJob, fExecTime / iNbJob))
        fSlope = (iNbJob * fSumProd - fSumX * fWall) / (iNbJob * fSumX2 - fSumX * fSumX)
        fOrd = (fWall - fSlope * fSumX) / iNbJob
        EDVerbose.screen("Regression of execution time: ExecTime = %.3f + %f * NbJob" % (fOrd, fSlope))


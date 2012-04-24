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
from __future__ import with_statement

__authors__ = ["Jérôme Kieffer", "Olof Svensson"]
__contact__ = "Jerome.Kieffer@ESRF.eu"
__license__ = "LGPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"
__date__ = "20110920"
__status__ = "production"

import threading, time, os, sys, gc
from EDVerbose              import EDVerbose
from EDFactoryPluginStatic  import EDFactoryPluginStatic
from EDFactoryPlugin        import EDFactoryPlugin
from EDLogging              import EDLogging
from EDSlot                 import EDSlot
from EDThreading import Semaphore
#asizeof does not work with Jython not with PyPy
if  (os.name == "java") or ("PyPy" in sys.version):
    asizeof = None
else:
    EDFactoryPluginStatic.loadModule("asizeof")
    import asizeof


class EDJob(EDLogging):
    """
    Create a module called EDJob
    * Most of what was done up to 09-2010 in EDParallelExecute should be done here
    * Each instance will be a job
    * Constructor takes a plugin name
    * Each instance will have taking an "setDataInput" method getting an XMLin (as string)
    * Each instance will gave a "getDataOutput" method with optional join 
    * there could be a "join" method, waiting for the job to finish
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
    PLUGIN_STATE_UNITIALIZED = "uninitialized"
    PLUGIN_STATE_RUNNING = "running"
    PLUGIN_STATE_SUCCESS = "success"
    PLUGIN_STATE_FAILURE = "failure"

    __edFactoryPlugin = EDFactoryPlugin()
    __dictJobs = {}
    __semaphore = Semaphore()
    __fStartTime = time.time()

    def __init__(self, _strPluginName):
        """
        Constructor of the class
        
        @param strPluginName: name of the plugin 
        @type strPluginName: string
        """
        EDLogging.__init__(self)
        self.__strPluginName = _strPluginName
        self.__edPlugin = None
        self.__edSlotCallBack = EDSlot()
        self.__edSlotSUCCESS = EDSlot()
        self.__edSlotFAILURE = EDSlot()
        self.__pathXSDInput = None
        self.__pathXSDOutput = None
        self.__bXmlInputSet = False
        self.__status = None
        self.__name = None
        self.__runtime = None
        self.__edPlugin = EDJob.__edFactoryPlugin.loadPlugin(self.__strPluginName)
        self.__jobId = "%s-%08i" % (self.__strPluginName, self.__edPlugin.getId())
        with self.__class__.__semaphore:
            self.__class__.__dictJobs[self.__jobId] = self
        if (self.__edPlugin is None):
            self.WARNING("Instantiation of plugin %s failed!!!" % _strPluginName)
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
        else:
            with self.locked():
                if (self.__edPlugin is not None):
                    self.__edPlugin.setDataInput(_oDataInput, _strDataInputKey)
                    self.__bXmlInputSet = True
                else:
                    self.WARNING("Setting DataInput for uninstanciated plugin %s." % self.__strPluginName)



    def getDataInput(self, _strDataInputKey=None):
        """
        Returns the Plugin Input Data for a particular key.
        If the key is not provided a default key is used.
        """
        if (self.__edPlugin is not None):
            return self.__edPlugin.getDataInput(_strDataInputKey).marshal()
        elif (self.__pathXSDInput is not None):
            return open(self.__pathXSDInput).read()
        else:
            self.WARNING("Getting DataInput for uninstanciated plugin %s." % self.__strPluginName)
    dataInput = property(getDataInput, setDataInput)


    def getDataOutput(self, _strDataOutputKey=None, _bWait=True):
        """
        Returns the Plugin Output Data
        @param _bWait: shall we wait for the plugin to finish to retrieve output data: Yes by default.
        @type _bWait: boolean
        """
        if _bWait: #Wait for plugin to finish befor returning data output
            self.synchronize()
        if (self.__edPlugin is not None):
            return self.__edPlugin.getDataOutput(_strDataOutputKey).marshal()
        elif self.__pathXSDOutput is not None:
            return open(self.__pathXSDOutput).read()
        else:
            self.WARNING("Getting DataOutput for uninstanciated plugin %s." % self.__strPluginName)
    dataOutput = property(getDataOutput)

    def execute(self):
        """
        Launch the EDNA plugin
        @return: JobId
        @rtype: string
        """
        if not self.__bXmlInputSet:
            self.WARNING("Not executing job %s as input is empty" % self.__jobId)

        if (self.__edPlugin is not None):
            with self.locked():
                self.__edPlugin.connectSUCCESS(self.successPluginExecution)
                self.__edPlugin.connectFAILURE(self.failurePluginExecution)
                self.__status = EDJob.PLUGIN_STATE_RUNNING
                self.__edPlugin.execute()
                return self.__jobId
        else:
            self.WARNING("Trying to run a plugin that does not exist: %s " % self.__strPluginName)


    def synchronize(self):
        """
        Synchronize the execution of the job with the calling thread.
        """
        with self.locked():
            strStatus = self.__status
        if strStatus == EDJob.PLUGIN_STATE_RUNNING:
            self.__edPlugin.synchronize()
        elif strStatus == EDJob.PLUGIN_STATE_UNITIALIZED:
            self.WARNING("Unable to synchronize %s jobs" % strStatus)
        else:
            self.DEBUG("Unable to synchronize %s jobs" % strStatus)


    @classmethod
    def synchronizeAll(cls):
        """
        Wait for all jobs to finish.
        """
        EDVerbose.DEBUG("EDJob.synchronizeAll class method ")
        listJob = cls.__dictJobs.keys()
        for jobid in listJob:
            job = cls.__dictJobs[jobid]
            job.synchronize()
        if len(cls.__dictJobs) != len(listJob):
            EDVerbose.WARNING("EDJob.synchronizeAll: New jobs have been launched while synchronizing")


    def successPluginExecution(self, _edObject=None):
        """
        Method called when the execution of the plugin succeeds 
        """
        with self.locked():
            self.__status = EDJob.PLUGIN_STATE_SUCCESS
            self.screen("Plugin %s: success after %.3fs" % (self.__jobId, _edObject.getRunTime()))
        try:
            self.__edSlotSUCCESS.call(self.__jobId)
        except Exception:
            self.ERROR("Error in execution of Success call-back for %s" % self.__jobId)
            self.writeErrorTrace()
        try:
            self.__edSlotCallBack.call(self.__jobId)
        except Exception:
            self.ERROR("Error in execution of Common call-back (after success) for %s" % self.__jobId)
            self.writeErrorTrace()


    def failurePluginExecution(self, _edObject=None):
        """
        Method called when the execution of the plugin failed 
        """
        with self.locked():
            self.__status = EDJob.PLUGIN_STATE_FAILURE
            self.screen("Plugin %s: failure after %.3fs" % (self.__jobId, _edObject.getRunTime()))
        try:
            self.__edSlotFAILURE.call(self.__jobId)
        except Exception:
            self.ERROR("Error in execution of Failure call-back for %s" % self.__jobId)
            self.writeErrorTrace()
        try:
            self.__edSlotCallBack.call(self.__jobId)
        except Exception:
            self.ERROR("Error in execution of Common call-back (after failure) for %s" % self.__jobId)
            self.writeErrorTrace()


    def connectSUCCESS(self, _oMethod):
        """
        @param _oMethod: function or method to be called - back
        """

        with self.locked():
            if (_oMethod != None):
                self.__edSlotSUCCESS.connect(_oMethod)


    def connectFAILURE(self, _oMethod):
        """
        @param _oMethod: function or method to be called - back
        """
        with self.locked():
            if (_oMethod != None):
                self.__edSlotFAILURE.connect(_oMethod)


    def connectCallBack(self, _oMethod):
        """
        @param _oMethod: function or method to be called - back
        """
        with self.locked():
            if (_oMethod != None):
                self.__edSlotCallBack.connect(_oMethod)


    def getJobId(self):
        """
        @return: JobId i.e. EDPluginName-Number
        @rtype: string
        """
        return self.__jobId
    jobId = property(getJobId, "EDJob.jobId: read-only property")
    getJobID = getJobId


    def getPluginName(self):
        """
        @return: Name of the plugin
        @rtype: string
        """
        return self.__strPluginName
    pluginName = property(getPluginName, "EDJob.pluginName: read-only property")


    def getPlugin(self):
        """
        @return: the plugin (instance)
        @rtype: python object
        """
        return self.__edPlugin
    plugin = property(getPlugin, "EDJob.plugin: read-only property")


    def getStatus(self):
        """
        @return: status of the Job
        @rtype: string
        """
        return self.__status
    status = property(getStatus, "EDJob.status: read-only property")


    def getName(self):
        return self.__name
    def setName(self, _strName):
        if self.__name is None:
            self.__name = _strName
        else:
            self.WARNING("EDJob.setName: One cannot rename a Job !!!")
    name = property(getName, setName, "EDJob.name: nickname of the job")



    def getMemSize(self):
        """
        try to guess the size in memory of a job
        @return: expected size in memory 
        """
        if asizeof is not None:
            return asizeof.asizeof(self)


    @classmethod
    def getStatusFromID(cls, jobId):
        """
        Retrieve the job (hence the plugin) status
        
        @param jobId: the Job identification number
        @type jobId: string
        @return: the EDJob status 
        @rtype: string 
        """
        if jobId in cls.__dictJobs:
            strRet = cls.__dictJobs[jobId].getStatus()
        else:
            strRet = "Unable to retrieve such job: %s" % jobId
            EDVerbose.WARNING(strRet)
        return strRet
    getStatusFromId = getStatusFromID


    @classmethod
    def getJobFromID(cls, jobId):
        """
        Retrieve the job (hence the plugin)
        
        @param jobId: the Job identification number
        @type jobId: string
        @return: the "EDJob instance", which contains the plugin (__edPlugin) and the status
        @rtype: a Python object. 
        """
        if jobId in cls.__dictJobs:
            return cls.__dictJobs[jobId]
        else:
            EDVerbose.WARNING("Unable to retrieve such EDJob: %s" % jobId)
    getJobFromId = getJobFromID


    @classmethod
    def getMemoryFootprint(cls):
        if asizeof is not None:
            return asizeof.asizesof(cls.__dictJobs)


    def cleanJob(self, forceGC=True):
        """
        Frees the memory associated with the top level plugin
        @param forceGC: Force garbage collection after clean-up
        @type forceGC: boolean
        """
        self.synchronize()
        with self.locked():
            if self.__edPlugin is not None:
                self.__pathXSDOutput = self.__edPlugin.strPathDataOutput
                self.__pathXSDInput = self.__edPlugin.strPathDataInput
                self.__runtime = self.__edPlugin.getRunTime()
                self.__edPlugin = None
        if forceGC:
            gc.collect()


    @classmethod
    def cleanJobfromId(cls, jobId, forceGC=True):
        """
        Frees the memory associated with the top level plugin
        
        @param jobId: the Job identification number
        @type jobId: string
        @param forceGC: Force garbage collection after clean-up
        @type forceGC: boolean
        """
        if jobId in cls.__dictJobs:
            job = cls.__dictJobs[jobId]
            job.cleanJob(forceGC)
            strRet = "Job %s cleaned" % jobId
        else:
            strRet = "Unable to retrieve such EDJob: %s" % jobId
            EDVerbose.WARNING(strRet)
        return strRet
    cleanJobfromID = cleanJobfromId


    @classmethod
    def getDataOutputFromId(cls, jobId):
        """
        Returns the Plugin Output Data
        @param jobId: job idenfier 
        @type jobId: string
        @return: edJob.DataOutput XML string
        """
        output = None
        job = cls.getJobFromId(jobId)
        if job is not None:
            output = job.getDataOutput()
        return output or ""
    getDataOutputFromID = getDataOutputFromId


    @classmethod
    def getDataInputFromId(cls, jobId):
        """
        Returns the Plugin Input Data
        @param jobId: job idenfier 
        @type jobId: string
        @return: edJob.DataInput XML string
        """
        output = None
        job = cls.getJobFromId(jobId)
        if job is not None:
            output = job.getDataInput()
        return output or ""
    getDataInputFromID = getDataInputFromId


    @classmethod
    def stats(cls):
        """
        Retrieve some statistics and print them
        """
        lstStrOut = []
        output = []
        fExecTime = time.time() - cls.__fStartTime
        keys = cls.__dictJobs.keys()
        keys.sort()
        for num, key in enumerate(keys) :
            job = cls.__dictJobs[key]
            if job.getPlugin() is None:
                runtime = job.__runtime
            else:
                runtime = job.getPlugin().getRunTime()
            output.append([num, key, job.getStatus(), runtime, job.getMemSize()])
        output.sort()
        iNbJob = max(1, len(keys))
        lstStrOut.append("_" * 110)
        lstStrOut.append("%s\t|\t%s\t\t\t\t|\t%s\t|\t%s\t\t|\t%s" % ("nr", "EDPluginName-Id", "status", "runtime", "memory"))
        lstStrOut.append("_" * 110)
        fWall = 0.0
        fSumProd = 0.0
        fSumX = 0.0
        fSumX2 = 0.0
        for oneJob in output:
            fWall += oneJob[3]
            fSumX += oneJob[0]
            fSumX2 += oneJob[0] * oneJob[0]
            fSumProd += oneJob[0] * oneJob[3]
            lstStrOut.append("%s\t|\t%s\t|\t%s\t|\t%9.3f\t|\t%s" % tuple(oneJob))
        lstStrOut.append("_" * 110)
        lstStrOut.append("Total execution time (Wall): %.3fs, Execution time: %.3fs. SpeedUp: %.3f" % (fWall, fExecTime, fWall / fExecTime))
        lstStrOut.append("Average execution time (Wall/N): %.3fs, Average throughput: %.3fs" % (fWall / iNbJob, fExecTime / iNbJob))
        if len(keys) > 1:
            fSlope = (iNbJob * fSumProd - fSumX * fWall) / (iNbJob * fSumX2 - fSumX * fSumX)
            fOrd = (fWall - fSlope * fSumX) / iNbJob
        else:
            fSlope = 0.0
            fOrd = fWall
        lstStrOut.append("Regression of execution time: ExecTime = %.3f + %f * NbJob" % (fOrd, fSlope))
        strOutput = os.linesep.join(lstStrOut)
        EDVerbose.screen(strOutput)
        return strOutput


#!/usr/bin/env python
# coding: utf8
#
#    Project: Tango Device Server
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C)2010 ESRF
#
#    Principal author:        Matias GUIJARRO (Matias.GUIJARRO@esrf.eu)
#                             Jérôme Kieffer  (jerome.kieffer@esrf.eu)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
from __future__ import with_statement

__authors__ = [ "Matias GUIJARRO", "Jérôme Kieffer", "Cyril Guilloud" ]
__contact__ = "jerome.kieffer@esrf.eu"
__license__ = "GPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"
__date__ = "20110919"
__status__ = "beta"

import sys, os, threading, gc, time
import PyTango
if sys.version > (3, 0):
    from queue import Queue
else:
    from Queue import Queue
# Append the EDNA kernel source directory to the python path
try:
    from rfoo.utils import rconsole
    rconsole.spawn_server()
except ImportError:
    print("No socket opened for debugging -> please install rfoo if you want to debug online")
else:
    print("rfoo installed, you can debug online with rconsole")

if not os.environ.has_key("EDNA_HOME"):
    strProgramPath = os.path.abspath(sys.argv[0])
    lPath = strProgramPath.split(os.sep)
    if len(lPath) > 3:
        strEdnaHomePath = os.sep.join(lPath[:-3])
    else:
        raise RuntimeError("Problem in the EDNA_HOME path ... %s" % strEdnaHomePath)
        sys.exit()
    os.environ["EDNA_HOME"] = strEdnaHomePath

sys.path.append(os.path.join(os.environ["EDNA_HOME"], "kernel", "src"))

from EDJob                  import EDJob
from EDLogging              import EDLogging
from EDVerbose              import EDVerbose
from EDUtilsParallel        import EDUtilsParallel
from EDStatus               import EDStatus
from EDFactoryPluginStatic  import EDFactoryPluginStatic


class EdnaDS(PyTango.Device_4Impl, EDLogging):
    """
    Tango device server launcher for EDNA server.
    """
    def __init__(self, cl, name):
        EDLogging.__init__(self)
        PyTango.Device_4Impl.__init__(self, cl, name)
        self.init_device()
        if isinstance(iNbCpu, int):
            self.screen("Initializing tangoDS with max %i jobs in parallel." % iNbCpu)
            self.__semaphoreNbThreads = threading.Semaphore(iNbCpu)
        else:
            self.__semaphoreNbThreads = threading.Semaphore(EDUtilsParallel.detectNumberOfCPUs())
        self.jobQueue = Queue()
        self.processingSem = threading.Semaphore()
        self.lastStatistics = "No statistics collected yet, please use the 'collectStatistics' method first"
        self.statLock = threading.Lock()
        self.lastFailure = None
        self.lastSuccess = None

    def delete_device(self):
        self.DEBUG("[Device delete_device method] for device %s" % self.get_name())

    def init_device(self):
        self.DEBUG("In %s.init_device()" % self.get_name())

        self.set_state(PyTango.DevState.ON)
        self.get_device_properties(self.get_device_class())
        self.set_change_event("jobSuccess", True, False)
        self.set_change_event("jobFailure", True, False)

    def always_executed_hook(self):
        pass

    def read_attr_hardware(self, data):
        self.DEBUG("In %s.read_attr_hardware()" % self.get_name())

    def read_jobSuccess(self, attr):
        self.DEBUG("In %s.read_jobSuccess()" % self.get_name())
        if self.lastSuccess is None:
            attr.set_value("No job succeeded (yet)")
        else:
            attr.set_value("Last success job: %s%s%s" % (self.lastSuccess, os.linesep, EDJob.getDataOutputFromId(self.lastSuccess)))

    def read_jobFailure(self, attr):
        self.DEBUG("In %s.read_jobFailure()" % self.get_name())
        if self.lastFailure is None:
            attr.set_value("No job Failed (yet)")
        else:
            attr.set_value("Last failed job: %s%s%s" % (self.lastFailure, os.linesep, EDJob.getDataOutputFromId(self.lastFailure)))

    def read_statisticsCollected(self, attr):
        attr.set_value(self.lastStatistics)

    def getJobState(self, jobId):
        return EDJob.getStatusFromID(jobId)

    def cleanJob(self, jobId):
        return EDJob.cleanJobFromID(jobId)

    def initPlugin(self, strPluginName):
        plugin = EDFactoryPluginStatic.loadPlugin(strPluginName)
        if plugin is None:
            return "Plugin not found: %s" % strPluginName
        else:
            return "Plugin loaded: %s" % strPluginName

    def abort(self, jobId):
        pass

    def quitEdna(self):
        self.DEBUG("In %s.quitEdna()" % self.get_name())
        self.screen("Quitting tango-EdnaDS")
        sys.exit()

    def startJob(self, argin):
        """
        @param argin: 2-list [ "EDPluginName", "<xml/><XSDataInputPluginName>...."]
        @return: jobID which is a sting: Plugin-000001
        """
        self.DEBUG("In %s.startJob()" % self.get_name())
        name, xsd = argin[:2]
        if xsd.strip() == "":
            return
        edJob = EDJob(name)
        if edJob is None:
            return "Error in load Plugin"
        jobId = edJob.getJobId()
        edJob.setDataInput(xsd)
        self.jobQueue.put(edJob)
        if self.processingSem._Semaphore__value > 0 :
            t = threading.Thread(target=self.startProcessing)
            t.start()
        return jobId

    def startProcessing(self):
        """
        Process all jobs in the queue.  
        """
        with self.processingSem:
            while not self.jobQueue.empty():
                self.__semaphoreNbThreads.acquire()
                edJob = self.jobQueue.get()
                edJob.connectSUCCESS(self.successJobExecution)
                edJob.connectFAILURE(self.failureJobExecution)
                edJob.execute()

    def successJobExecution(self, jobId):
        self.DEBUG("In %s.successJobExecution(%s)" % (self.get_name(), jobId))
        with self.locked():
            self.__semaphoreNbThreads.release()
            EDJob.cleanJobfromID(jobId, False)
            self.lastSuccess = jobId
            self.push_change_event("jobSuccess", jobId)
            gc.collect()

    def failureJobExecution(self, jobId):
        self.DEBUG("In %s.failureJobExecution(%s)" % (self.get_name(), jobId))
        with self.locked():
            self.__semaphoreNbThreads.release()
            EDJob.cleanJobfromID(jobId, False)
            self.lastFailure = jobId
            self.push_change_event("jobFailure", jobId)
            sys.stdout.flush()
            sys.stderr.flush()
            gc.collect()

    def getRunning(self):
        """
        retrieve the list of plugins currently under execution (with their plugin-Id)
        """
        return EDStatus.getRunning()

    def getSuccess(self):
        """
        retrieve the list of plugins finished with success (with their plugin-Id)
        """
        return EDStatus.getSuccess()

    def getFailure(self):
        """
        retrieve the list of plugins finished with failure (with their plugin-Id)
        """
        return EDStatus.getFailure()

    def collectStatistics(self):
        """
        Retrieve some statistics on all EDNA-Jobs
        @return: a page of information about EDNA-jobs
        """
        t = threading.Thread(target=self.statistics)
        t.start()


    def statistics(self):
        """
        retrieve some statistics about past jobs.
        """
        with self.statLock:
            fStartStat = time.time()
            self.lastStatistics = EDJob.stats()
            self.lastStatistics += os.linesep + "Statistics collected on %s, the collect took: %.3fs" % (time.asctime(), time.time() - fStartStat)
            self.push_change_event("statisticsCollected", self.lastStatistics)


    def getStatistics(self):
        """
        just return statistics previously calculated 
        """
        return  self.lastStatistics

    def getJobOutput(self, jobId):
        """
        Retrieve XML output form a job
        @param jobId: name of the job
        @return: output from a job        
        """
        return EDJob.getDataOutputFromId(jobId)

    def getJobInput(self, jobId):
        """
        Retrieve XML input from a job
        @param jobId: name of the job
        @return: xml input from a job        
        """
        return EDJob.getDataInputFromId(jobId)

class EdnaDSClass(PyTango.DeviceClass):
    #    Class Properties
    class_property_list = {
        }

    #    Device Properties
    device_property_list = {
        'plugins_directory':
            [PyTango.DevString,
            "EDNA plugins directory",
            [] ],
        }


    #    Command definitions
    cmd_list = {
        'startJob': [[PyTango.DevVarStringArray, "[<EDNA plugin to execute>,<XML input>]"], [PyTango.DevString, "job id"]],
        'abort': [[PyTango.DevString, "job id"], [PyTango.DevBoolean, ""]],
        'getJobState': [[PyTango.DevString, "job id"], [PyTango.DevString, "job state"]],
        "initPlugin": [[PyTango.DevString, "plugin name"], [PyTango.DevString, "Message"]],
        "cleanJob":[[PyTango.DevString, "job id"], [PyTango.DevString, "Message"]],
        "collectStatistics":[[PyTango.DevVoid, "nothing needed"], [PyTango.DevVoid, "Collect some statistics about jobs within EDNA"]],
        "getStatistics":[[PyTango.DevVoid, "nothing needed"], [PyTango.DevString, "Retrieve statistics about EDNA-jobs"]],
        'getJobOutput': [[PyTango.DevString, "job id"], [PyTango.DevString, "job output XML"]],
        'getJobInput': [[PyTango.DevString, "job id"], [PyTango.DevString, "job input XML"]],
        }


    #    Attribute definitions
    attr_list = {
        'jobSuccess':
            [[PyTango.DevString,
            PyTango.SCALAR,
            PyTango.READ]],
        'jobFailure':
            [[PyTango.DevString,
            PyTango.SCALAR,
            PyTango.READ]],
        "statisticsCollected":
            [[PyTango.DevString,
            PyTango.SCALAR,
            PyTango.READ]],
    }

    def __init__(self, name):
        PyTango.DeviceClass.__init__(self, name)
        self.set_type(name);
        EDVerbose.DEBUG("In EdnaDSClass  constructor")

if __name__ == '__main__':

    EDVerbose.screen("Starting EDNA Tango Device Server")
    ltangoParam = ["EdnaDS"]
    iNbCpu = None
    for oneArg in sys.argv[1:]:
        if oneArg.lower().find("-debug") > 0:
            EDVerbose.setVerboseOn()
            EDVerbose.setVerboseDebugOn()
        elif oneArg.lower().find("-ncpu=") > 0:
            iNbCpu = int(oneArg.split("=")[1])
        else:
           ltangoParam.append(oneArg)
    EDUtilsParallel.initializeNbThread()
    try:
        print ltangoParam
        py = PyTango.Util(ltangoParam)
        py.add_TgClass(EdnaDSClass, EdnaDS, 'EdnaDS')
        U = py.instance() #PyTango.Util.instance()
        U.server_init()
        U.server_run()
    except PyTango.DevFailed, e:
        EDVerbose.ERROR('PyTango --> Received a DevFailed exception: %s' % e)
        sys.exit(-1)
    except Exception, e:
        EDVerbose.ERROR('PyTango --> An unforeseen exception occurred....%s' % e)
        sys.exit(-1)

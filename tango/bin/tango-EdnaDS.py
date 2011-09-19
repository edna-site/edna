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
"""
Tango device server launcher for EDNA server.
"""

__authors__ = [ "Matias GUIJARRO", "Jérôme Kieffer", "Cyril Guilloud" ]
__contact__ = "jerome.kieffer@esrf.eu"
__license__ = "GPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"
__date__ = "20110919"
__satatus__ = "beta"

import sys, os, threading
import PyTango

# Append the EDNA kernel source directory to the python path

if not os.environ.has_key("EDNA_HOME"):
    strProgramPath = os.path.abspath(sys.argv[0])
    lPath = strProgramPath.split(os.sep)
    if len(lPath) > 3:
        strEdnaHomePath = os.sep.join(lPath[:-3])
    else:
        EDVerbose.ERROR("Problem in the EDNA_HOME path ... %s" % strEdnaHomePath)
        sys.exit()
    os.environ["EDNA_HOME"] = strEdnaHomePath

sys.path.append(os.path.join(os.environ["EDNA_HOME"], "kernel", "src"))

from EDJob              import EDJob
from EDLogging          import EDLogging
from EDVerbose          import EDVerbose
from EDUtilsParallel    import EDUtilsParallel
from EDStatus           import EDStatus

class EdnaDS(PyTango.Device_4Impl, EDObject):
    def __init__(self, cl, name):
        EDLogging.__init__(self)
        PyTango.Device_4Impl.__init__(self, cl, name)
        self.init_device()
        self.__iNbThreads = EDUtilsParallel.detectNumberOfCPUs(_iNbThreads)
        EDUtilsParallel.initializeNbThread(self.__iNbThreads)
        self.__semaphoreNbThreads = threading.Semaphore(self.__iNbThreads)


    def delete_device(self):
        EDVerbose.DEBUG("[Device delete_device method] for device %s" % self.get_name())

    def init_device(self):
        EDVerbose.DEBUG("In %s.init_device()" % self.get_name())

        self.set_state(PyTango.DevState.ON)
        self.get_device_properties(self.get_device_class())
        self.set_change_event("jobSuccess", True, False)
        self.set_change_event("jobFailure", True, False)

    def always_executed_hook(self):
        pass

    def read_attr_hardware(self, data):
        EDVerbose.DEBUG("In %s.read_attr_hardware()" % self.get_name())

    def read_jobSuccess(self, attr):
        EDVerbose.DEBUG("In %s.read_jobSuccess()" % self.get_name())
        attr.set_value("")

    def read_jobFailure(self, attr):
        attr.set_value("")

    def getJobState(self, jobId):
        return EDJob.getStatusFromID(jobId) or "unknown job"

    def abort(self, jobId):
        pass

    def quitEdna(self):
        EDVerbose.DEBUG("In %s.quitEdna()" % self.get_name())
        EDVerbose.screen("Quitting tango-EdnaDS")
        sys.exit()

    def startJob(self, argin):
        """
        @param argin: 2-list [ "EDPluginName", "<xml/><XSDataInputPluginName>...."]
        @return: jobID which is a sting: Plugin-000001
        """
        self.DEBUG("In %s.startJob()" % self.get_name())
        edJob = EDJob(argin[0])
        jobId = edJob.getJobId()
        myThread = threading.Thread(target=self.startThread, name=jobId, args=[edJob, argin[1]])
        myThread.start()
        return jobId

    def startThread(self, edJob, strXmlIn):
        """
        Thread launching the job itself.
        """
        self.__semaphoreNbThreads.acquire()
        edJob.setDataInput(strXmlInput)
        edJob.connectSUCCESS(self.successJobExecution)
        edJob.connectFAILURE(self.failureJobExecution)
        edJob.execute()

    def successJobExecution(self, jobId):
        self.DEBUG("In %s.successJobExecution(%s)" % (self.get_name(), jobId))
        with self.lock():
            self.__semaphoreNbThreads.release()
            self.push_change_event("jobSuccess", jobId)

    def failureJobExecution(self, jobId):
        self.DEBUG("In %s.failureJobExecution(%s)" % (self.get_name(), jobId))
        with self.lock():
            self.__semaphoreNbThreads.release()
            self.push_change_event("jobFailure", jobId)

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
    }

    def __init__(self, name):
        PyTango.DeviceClass.__init__(self, name)
        self.set_type(name);
        self.DEBUG("In EdnaDSClass  constructor")

if __name__ == '__main__':

    EDVerbose.screen("Starting EDNA Tango Device Server")
    ltangoParam = ["EdnaDS"]
    iNbCpu = None
    for oneArg in sys.argv[1:]:
        if oneArg.lower().find("-debug") > 0:
            EDVerbose.setVerboseOn()
        elif oneArg.lower().find("-ncpu=") > 0:
            iNbCpu = int(oneArg.split("=")[1])
        else:
           ltangoParam.append(oneArg)
    EDUtilsParallel.initializeNbThread(iNbCpu)
    try:
        print ltangoParam
        py = PyTango.Util(ltangoParam)
        py.add_TgClass(EdnaDSClass, EdnaDS, 'EdnaDS')
        U = py.instance() #PyTango.Util.instance()
#        for x in dir(U):
#          try:
#            xx = getattr(U, x)
#            EDVerbose.screen( x, xx()
#          except:
#            continue
        U.server_init()
        U.server_run()
    except PyTango.DevFailed, e:
        EDVerbose.ERROR('PyTango --> Received a DevFailed exception:', e)
        sys.exit(-1)
    except Exception, e:
        EDVerbose.ERROR('PyTango --> An unforeseen exception occurred....', e)
        sys.exit(-1)

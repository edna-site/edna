#!/usr/bin/env python
# -*- coding: utf8 -*-
#
#    Project: BioSaxs
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) European Synchrotron Radiation Facility, Grenoble, France
#
#    Principal author:       Jérôme Kieffer (Jerome.Kieffer@ESRF.eu)
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

__author__ = "Jérôme Kieffer"
__contact__ = "Jerome.Kieffer@ESRF.eu"
__license__ = "GPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"
__date__ = "20120924"

import os, sys, time, threading, gc
if sys.version > (3, 0):
    from queue import Queue
else:
    from Queue import Queue

# Append the EDNA kernel source directory to the python path
if "EDNA_HOME" not in os.environ:
    pyStrProgramPath = os.path.abspath(__file__)
    pyLPath = pyStrProgramPath.split(os.sep)
    if len(pyLPath) > 3:
        pyStrEdnaHomePath = os.sep.join(pyLPath[:-3])
    else:
        print ("Problem in the EDNA_HOME path ..." + pyStrEdnaHomePath)
        sys.exit()
    os.environ["EDNA_HOME"] = pyStrEdnaHomePath

sys.path.append(os.path.join(os.environ["EDNA_HOME"], "kernel", "src"))
from EDLogging import EDLogging
from EDFactoryPluginStatic  import EDFactoryPluginStatic
from EDJob import EDJob
from EDThreading import Semaphore
from EDUtilsParallel import EDUtilsParallel
from EDStatus import EDStatus

class Reprocess(EDLogging):
    def __init__(self, strPluginName, iNbCpu=None):
        EDLogging.__init__(self)
        self.pluginName = strPluginName
        self.startTime = time.time()
        try:
            self.iNbCpu = int(iNbCpu)
        except:
            self.iNbCpu = EDUtilsParallel.detectNumberOfCPUs()

        self.screen("Initializing Reprocess with max %i jobs in parallel." % self.iNbCpu)
        self.__semaphoreNbThreads = Semaphore(self.iNbCpu)
        EDUtilsParallel.initializeNbThread(self.iNbCpu)
        self.jobQueue = Queue()
        self.processingSem = Semaphore()
        self.statLock = Semaphore()
        self.lastStatistics = "No statistics collected yet, please use the 'collectStatistics' method first"
        self.lastFailure = "No job Failed (yet)"
        self.lastSuccess = "No job succeeded (yet)"


    def startJob(self, xsd):
        """
        @param xsd: XML data structure as a string or path to a string
        @return: jobID which is a sting: Plugin-000001
        """
        self.DEBUG("In %s.startJob()" % self.__class__.__name__)
        if xsd.strip() == "":
            return
        if os.path.isfile(xsd):
            xsd = open(xsd, "rb").read()
        edJob = EDJob(self.pluginName)
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
        self.DEBUG("In %s.successJobExecution(%s)" % (self.__class__.__name__, jobId))
        with self.locked():
            self.__semaphoreNbThreads.release()
            EDJob.cleanJobfromID(jobId, False)
            self.lastSuccess = jobId
            gc.collect()

    def failureJobExecution(self, jobId):
        self.DEBUG("In %s.failureJobExecution(%s)" % (self.__class__.__name__, jobId))
        with self.locked():
            self.__semaphoreNbThreads.release()
            EDJob.cleanJobfromID(jobId, False)
            self.lastFailure = jobId
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
        return self.lastStatistics

    def getStatistics(self):
        """
        just return statistics previously calculated
        """
        return self.lastStatistics

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

    def join(self):
        """
        wait for all jobs to finish
        """
        while not (self.jobQueue.empty() and \
                (self.__semaphoreNbThreads._Semaphore__value == self.iNbCpu) and \
                (EDUtilsParallel.getNbRunning() == 0) and \
                (self.processingSem._Semaphore__value == 1) and\
                (len(EDStatus.getRunning()) == 0)):
            time.sleep(1)


if __name__ == "__main__":
    res = {}
    def sortn(a, b):
        if res[a][1] < res[b][1]:
            return 1
        else:
            return -1

    from optparse import OptionParser
    parser = OptionParser(usage="%prog reprocess on SAXS-HPLC experiment", version="%prog 1.0")
#    parser.add_option("-o", "--output", dest="h5path",
#                      help="put loh information to ")
#    parser.add_option("-c", "--crop", dest="crop",
#                      help="Shall we crop the dataset to valid area", default=True)
#    parser.add_option("-k", "--check", dest="recheck",
#                      help="Shall we recheck the consistency of the various frames ... very time consuming !!! (not implemented", default=False)
    parser.add_option("-n", "--ncpu", dest="ncpu", action="store", type="int",
                      help="limit the number of CPU used", default=None)
    parser.add_option("-d", "--debug",
                      action="store_true", dest="verbose", default=False,
                      help="switch to debug mode")
    parser.add_option("-p", "--plugin", action="store", type="string",
                      dest="plugin", default="EDPluginBioSaxsHPLCv1_0",
                      help="use an alternative plugin")
    parser.add_option("-y", "--yappi", action="store_true",
                      dest="yappi", default=False,
                      help="use an multi-threaded profiler named 'YAPPI'")
    (options, args) = parser.parse_args()
    print("")
    print("Options:")
    print('========')
    for k, v in options.__dict__.items():
        print("    %s: %s" % (k, v))
    print("")
    if len(args) > 5:
        print("Input XML files: " + ", ".join([f for f in list(args) if f.endswith(".xml")][:5]) + "...")
    else:
        print("Input XML files: " + ", ".join([f for f in list(args) if f.endswith(".xml")]))
    print(" ")
    reprocess = Reprocess(options.plugin, options.ncpu)
    if options.yappi:
        try:
            import yappi
        except ImportError:
            print("Sorry, I was not able to import Yappi")
            yappi = None
    else:
        yappi = None
    if options.verbose:
        reprocess.setVerboseDebugOn()
    fullargs = [os.path.abspath(i) for i in args if os.path.exists(i) and i.endswith(".xml")]
    working_dir = "Reprocess-HPLC-%s" % time.strftime("%Y%m%d-%H%M%S")
    os.makedirs(working_dir)
    os.chdir(working_dir)
    if yappi: yappi.start()
    for i in fullargs:
        reprocess.startJob(i)
    print("All %i jobs queued after %.3fs" % (len(args), time.time() - reprocess.startTime))
    reprocess.join()
    if yappi: yappi.stop()
    print("All %i jobs processed after %.3fs" % (len(args), time.time() - reprocess.startTime))
    print reprocess.statistics()
    if yappi:
        stat = yappi.get_stats(sort_type=yappi.SORTTYPE_TTOT)
        res = {}
        for i in stat.func_stats:
            if i[0] in res:
                res[i[0]][0] += i[1]
                res[i[0]][1] += i[2]
            else:
                res[i[0]] = [i[1], i[2]]
        keys = res.keys()
        keys.sort(sortn)
        with open("yappi.out", "w") as f:
            f.write("ncall\t\ttotal\t\tpercall\t\tfunction%s" % (os.linesep))
            for i in keys:
                f.write("%8s\t%16s\t%16s\t%s%s" % (res[i][0], res[i][1], res[i][1] / res[i][0], i, os.linesep))
        print("Profiling information written in yappi.out")
    edJob = EDJob("EDPluginBioSaxsFlushHPLCv1_0")
    edJob.setDataInput(open(fullargs[-1], "r").read())
    edJob.execute()


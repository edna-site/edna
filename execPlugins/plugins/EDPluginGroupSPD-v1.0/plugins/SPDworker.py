#!/usr/bin/env python
#    Project: EDNA Exec Plugins
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2008-2010 ESRF
#
#    Principal authors:      Jerome Kieffer (kieffer@esrf.fr)
#                            
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
""" 
This is piece of software provides an interface to the SPD program 
which will be running in server mode, waiting for command on stdin 
"""

__author__ = "Jerome Kieffer"
__contact__ = "Jerome.Kieffer@esrf.eu"
__license__ = "GPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"

import os, time, subprocess, signal, threading, sys

#DEBUG = True

class SPDworker():
    """
    This is a class representing an SPD worker, i.e. it's configures the program, start, get its PID, ...
    """
    def __init__(self):
        """
        Constructor of the class
        """
        self.executable = "/sware/exp/scisoft/spd/v1.2/LINUX64/spd"
        self.semaphore = threading.Semaphore()
        self.status = "uninitialized"
        self.startTime = time.time()
        self.timeOut = 100
        self._proc = None
        self.pid = None
        self.config = None
        self.logFilename = None
        self.logFile = sys.stderr


    def  __repr__(self):
        return "SPDworker from %s using spd binary from %s pid=%s, last calculation currently in status %s and semaphore value %s"\
        % (__file__, self.executable, self.pid, self.status, self.semaphore._Semaphore__value)


    def initialize(self, strConf):
        """
        Method for running SPD, getting it's PID, ... should be fast as there are no calculation launched at this step.
        @param   strConf: a string representing the configuration of SPD (without any file to process)
        @type    strConf: string  
        """
#        print "initialize " + strConf
        if self.status in ["working", "initializing"]:
            self.kill()
        self.setConfig(strConf)
#        print "initialize after setConfig: %s %s" % (self.status, self._proc)
        if (self.status == "uninitialized") or (self._proc == None) or (self._proc.poll() is not None):
            self.semaphore.acquire()
            if self.logFilename == None:
                self.logFile = sys.stderr
            else:
                self.logFile = open(self.logFilename, "a")
            self._proc = subprocess.Popen ([self.executable, "--server"],
                                           stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                           shell=False, bufsize=0)
            self.pid = self._proc.pid
            self.logFile.write("log: SPD server started %s has PID %i \n" % (time.asctime(), self.pid))
            result = self._proc.stdout.readline()
            if result.strip() == "Server Mode":
                self.logFile.write("log: spd said " + result)
            else:
                self.logFile.write("err: spd said " + result)
            self.semaphore.release()
#        else:
#            result = "Server Mode"
        self.status = "initializing"

#        if DEBUG: self.logFile.write(self.__repr__() + os.linesep)
        self.logFile.flush()



    def kill(self, gentle=False):
        """
        Method to finish the SPD process the best way possible :/
        @param: gentle: if True, tries to communicate with the process to quit the best way, if not, use "kill"
        @type gentle: boolean  
        """
        self.logFile.write("log: kill method called on %s, previous status was %s \n" % (time.asctime(), self.status))
        if self._proc is None:
            self.status = "uninitialized"
            return
        if gentle:
            timer = threading.Timer(1, self.kill)
            timer.start()
            try:
                self._proc.stdin.write("--exit\n")
                self._proc.stdin.flush()
            except IOError:
                pass
            timer.cancel()
        try:
            if self._proc.poll() is None:
                os.kill(self.pid, signal.SIGINT)
                time.sleep(1)
                if self._proc.poll() is None:
                    os.kill(self.pid, signal.SIGTERM)
                    time.sleep(1)
                    if self._proc.poll() is None:
                        os.kill(self.pid, signal.SIGKILL)
            self.logFile.write("log: SPD returned with code %s \n" % (self._proc.poll()))
        except AttributeError:
            #meens something else killed the process during that time ... 
            pass
        self._proc = None
        self.status = "uninitialized"
#        if DEBUG: self.logFile.write(self.__repr__() + os.linesep)
        self.logFile.flush()


    def process(self, filename):
        """
        process one file througth SPD
        @param filename: the name of the file to process
        @type filename: python string
        @return : log of the in/out communication
        @rtype: dict of string
        """

        if self.status == "uninitialized":
            self.initialize(self.config)
        self.semaphore.acquire()

        bTimeOut = False
        bRetError = False

        if self.status == "initializing":
            args = "%s %s\n" % (self.config, filename)
        else:
            args = filename + "\n"
        while  (self.status == "working"):
            time.sleep(1)
            self.logFile.write("wrn: process while worker is still working.")
        self.status = "working"
        self.logFile.write("inp: " + args)
        dictReturn = {}
        self.startTime = time.time()
        timer = threading.Timer(self.timeOut, self.kill)
        timer.start()
        self._proc.stdin.write(args)
        self._proc.stdin.flush()
        bprocessing = True
        while bprocessing:
            if self._proc is None:

                self.logFile.write("err: SPD crashed without returned Code\n")
                bRetError = True
                bprocessing = False
                break
            else:
                retCode = self._proc.poll()
                if retCode  is not None:
                    self.logFile.write("err: SPD crashed with returned code: %s\n" % retCode)
                    for strout in self._proc.stdout.readlines():
                        self.logFile.write("out: " + strout)
                    for strerr in self._proc.stderr.readlines():
                        self.logFile.write("err: " + strerr)
                    bprocessing = False
                    bRetError = True
                    break
            strOut = self._proc.stdout.readline()
            self.logFile.write("out: " + strOut)
            if strOut.find ("ERROR:") == 0:
                if not (strOut.find ('ERROR: missing keyword "BINNING" in file') == 0):
                    bRetError = True
            elif strOut.find("Image processing took") == 0:
                bprocessing = False
            elif strOut.find("Saving") == 0:
                words = strOut.split()
                dictReturn[words[1] ] = os.path.abspath(words[-1])
        timer.cancel()
        try:
            self._proc.stderr.flush()
        except AttributeError:
            self.kill()
            bRetError = True
        if time.time() - self.startTime >= self.timeOut :
            bTimeOut = True
            self.logFile.write("err: TIMEOUT: SPD Calculation timeout is %.3f s\n" % (self.timeOut))
        self.logFile.write("log: SPD Calculation on %s took %.3f s\n" % (filename, time.time() - self.startTime))
        dictReturn["timeout"] = bTimeOut
        dictReturn["error"] = bRetError
#        if DEBUG:
#            self.logFile.write(self.__repr__() + os.linesep)
        self.logFile.write(str(dictReturn) + os.linesep)
        self.logFile.flush()
        self.status = "free"
        self.semaphore.release()
        return dictReturn


    def getStatus(self):
        """
        Getter for the status of the SPD worker under control
        @rtype: string
        @return: worker is +uninitialized, initializing, free, working ...
        """

        if self._proc is None:
            self.status = "uninitialized"
        else:
            if  self._proc.poll() is not None:
                self.kill()
        #self.logFile.write("log: worker status = %s \n" % self.status)
        #self.logFile.flush()
        return self.status

    def getConfig(self):
        """getter for the configuration
        @return: the string which was passed to SPD to set-up the program  
        @rtype: string
        """
        return self.config

    def setConfig(self, strConfig):
        """
        Setter for the configuration of the SPD worker
        @param strConfig: the string which will be passed to SPD to set-up the program  
        @type strConfig: string
        """
        self.config = strConfig

    def setTimeOut(self, timeout):
        """
        Setter for time-out
        @param timeout: value in seconds of the time-out
        @type timeout: float
        """
        if self.logFile:
            self.logFile.write("log: Set TimeOut to  %.3f s \n" % timeout)
        self.timeOut = timeout

    def getTimeOut(self):
        """
        Getter for time-out
        @return: time-out in seconds
        @rtype: : float
        """
        return self.timeOut

    def setExecutable(self, strExecutable):
        """
        Setter for the program to execute with its default options like spd --server
        @param strExecutable: full path of the program to execute with default options
        @type strExecutable: string
        """
        self.executable = strExecutable

    def getExecutable(self):
        """
        getter for the executable 
        @return: the path of the compiled program (spd) witch is in use 
        @rtype: string
        """
        return self.executable

    def setLogFilename(self, strfilename):
        """
        Setter for the filename.
        The initialization of the file will only take place in int initialize method
        @param filename: the name of file witch will contain the logs
        @type filename: string  
        """
        self.logFilename = strfilename

    def getLogFilename(self):
        """
        getter for the filename
        @return: the name of the log file
        @rtype: string  
        """
        return self.logFilename

    def closeLogFile(self):
        """
        Closes the log file.
        """
        self.logFile.write("end: Closing logfile on %s" % time.asctime())
        if self.logFile != sys.stderr:
            self.logFile.close()
        self.logFile = sys.stderr

if __name__ == '__main__':
    worker = SPDworker()
    worker.setExecutable("/sware/exp/scisoft/spd/v1.2/LINUX64/spd")
    image = os.path.join(os.environ["EDNA_HOME"], "tests", "data", "images", "MokeImage-2th21-tilt3-rot30.edf")
#    worker.kill()
#    print worker.getStatus()
#    worker.initialize("verbose=0 flat_distortion=0  src_ext=edf cor_ext=cor cen_1=1.050000e+03 cen_2=1.000000e+03 \
#                       dis=1.000000e-01 pix_1=4.722438e-05 pix_2=4.683152e-05 do_dark=0  do_distortion=2\
#                       xfile=example-tilted-t3-p30-d100-x.edf yfile=example-tilted-t3-p30-d100-y.edf")
#    print worker.getStatus()
#    print worker.process("MokeImage-2th10-tilt3-rot30.edf")
#    #os.system("ps aux |grep spd")
#    print worker.getStatus()
#    #print worker.kill()
#    print worker.getStatus()
#    print worker.getConfig()
#    print worker.getExecutable()
##    worker.setTimeOut(1)
#    print worker.process("MokeImage-2th12-tilt3-rot30.edf")
    print worker.getStatus()
    worker.initialize("flat_distortion=0 cen_1=1.050000e+03 cen_2=1.000000e+03 dis=1.000000e-01\
     pix_1=4.722438e-05 pix_2=4.683152e-05 do_dark=0  do_distortion=2 distortion_file=%s/tests/data/images/frelon_spline_file_to_correct_SPD.spline" % os.environ["EDNA_HOME"])
    print worker.getStatus()
#    t = threading.Timer(100, worker.kill)
#    t.start()
    print worker.process(image)
#    t.cancel()
    print worker.getStatus()
#    worker.kill()
#    print worker.getStatus()
#    print worker.process("MokeImage-2th19-tilt3-rot30.edf")
#    print worker.getStatus()
#    worker.kill()
    #worker.setTimeOut(1)
    print worker.process(image)
#    t = threading.Timer(1, worker.kill)
#    t.start()
    print worker.getStatus()
    print worker.process(image)
    print worker.getStatus()
#    worker.kill()
    print worker.getStatus()
    print worker.process(image)
    print worker.getStatus()

    worker.kill(True)
    print "switch to development version of SPD ....."
    print "*" * 60
    worker.setExecutable(os.environ["HOME"] + "/workspace/azimuthal/spd/runtime/LINUX64/spd")
    print worker.getStatus()
    worker.initialize("flat_distortion=0 cen_1=1.050000e+03 cen_2=1.000000e+03 dis=1.000000e-01\
     pix_1=4.722438e-05 pix_2=4.683152e-05 do_dark=0  do_distortion=2 distortion_file=%s/tests/data/images/frelon_spline_file_to_correct_SPD.spline" % os.environ["EDNA_HOME"])
    print worker.getStatus()
    print worker.process(image)

    print worker.getStatus()
    print worker.process(image)
    print worker.getStatus()
    print worker.process(image)
    print worker.getStatus()
    print worker.process(image)

    print worker.getStatus()
    worker.kill(True)

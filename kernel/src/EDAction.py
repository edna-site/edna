# coding: utf8
#
#    Project: The EDNA Kernel
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2008-2009 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal authors: Olof Svensson (svensson@esrf.fr) 
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

#
# This class has been inspired by the corresponding AALib class 
# (20090518-PyAALib-JyAALib-111) and modified according to the needs 
# for the EDNA project.
#

__authors__ = [ "Olof Svensson", "Jérôme Kieffer" ]
__contact__ = "svensson@esrf.fr"
__license__ = "LGPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"

"""
This class is taking care of the workflow preProcess - process - postProcess.
"""


import time, os
from threading   import Thread
from EDSlot      import EDSlot
from EDVerbose   import EDVerbose
from EDLogging   import EDLogging


class EDAction(EDLogging, Thread):
    """
    This class is taking care of executing the EDNA plugin and
    application workflow preProcess - process - postProcess.
    The detailed workflow looks like this:
    
    preProcess
    if not failure: slotPreProcess 
    if not failure: process 
    if not failure: slotProcess 
    if not failure: postProcess 
    if not failure: slotPostProcess
    if not failure: slotSUCCESS 
    if failure: slotFAILURE 
    Always: finally Process 
    """

    def __init__(self):
        EDLogging.__init__(self)
        Thread.__init__(self)
        self.__edSlotPreProcess = EDSlot()
        self.__edSlotProcess = EDSlot()
        self.__edSlotPostProcess = EDSlot()
        self.__edSlotSUCCESS = EDSlot()
        self.__edSlotFAILURE = EDSlot()
        self.__edSlotFinallyProcess = EDSlot()
        self.__bIsFailure = False
        self.__bIsTimeOut = False
        self.__fTimeOutInSeconds = None
        self.__fDefaultTimeOutInSeconds = 600.0
        self.__bIsAbort = False
        # Reference to the object which calls execute or executeSynchronous
        self.__edObject = None
        self.__lExtraTime = [] # list of extra allowed time for execution (in second)
        self.__bLogTiming = False

    def executeKernel(self):
        dictTimeStamps = { "init": time.time() }
        self.setTimeInit()
        try:

            if (not self.isFailure()):
                self.DEBUG("EDAction.executeKernel preProcess " + self.getClassName())
                self.preProcess()
                if self.__bLogTiming:
                    dictTimeStamps["preProcess"] = time.time()

            if (not self.isFailure()):
                self.DEBUG("EDAction.executeKernel slotPreProcess " + self.getClassName())
                self.__edSlotPreProcess.call(self)
                if self.__bLogTiming:
                    dictTimeStamps["slotPreProcess"] = time.time()

            if (not self.isFailure()):
                self.DEBUG("EDAction.executeKernel process " + self.getClassName())
                self.process()
                if self.__bLogTiming:
                    dictTimeStamps["process"] = time.time()

            if (not self.isFailure()):
                self.DEBUG("EDAction.executeKernel slotProcess " + self.getClassName())
                self.__edSlotProcess.call(self)
                if self.__bLogTiming:
                    dictTimeStamps["slotProcess"] = time.time()

            if (not self.isFailure()):
                self.DEBUG("EDAction.executeKernel postProcess " + self.getClassName())
                self.postProcess()
                if self.__bLogTiming:
                    dictTimeStamps["postProcess"] = time.time()

            if (not self.isFailure()):
                self.DEBUG("EDAction.executeKernel slotPostProcess " + self.getClassName())
                self.__edSlotPostProcess.call(self)
                if self.__bLogTiming:
                    dictTimeStamps["slotPostProcess"] = time.time()

        except Exception:
            self.writeErrorTrace()
            self.setFailure()

        # Execute finally process even in case of failure
        self.DEBUG("EDAction.executeKernel finallyProcess" + self.getClassName())
        try:
            self.finallyProcess()
            if  self.__bLogTiming:
                dictTimeStamps["finallyProcess"] = time.time()
        except Exception:
            self.DEBUG("EDAction.executeKernel: ERROR in finallyProcess!")
            self.writeErrorTrace()
            self.setFailure()
        try:
            self.__edSlotFinallyProcess.call(self)
        except Exception:
            self.DEBUG("EDAction.executeKernel: ERROR in slotFinallyProcess!")
            self.writeErrorTrace()
            self.setFailure()

        if (not self.isFailure()):
            self.DEBUG("EDAction.executeKernel slotSUCCESS")
            # Check that something doesn't go wrong in the success method!
            try:
                self.__edSlotSUCCESS.call(self)
                if  self.__bLogTiming:
                    dictTimeStamps["slotSUCCESS"] = time.time()

            except Exception:
                self.DEBUG("EDAction.executeKernel: ERROR in slotSUCCESS!")
                self.writeErrorTrace()
                self.setFailure()

        if (self.isFailure()):
            self.DEBUG("EDAction.executeKernel slotFAILURE")
            # Check that something doesn't go wrong in the success method!
            try:
                self.__edSlotFAILURE.call(self)
                if  self.__bLogTiming:
                    dictTimeStamps["slotFAILURE"] = time.time()
            except Exception:
                self.DEBUG("EDAction.executeKernel: ERROR in slotFAILURE!")
                self.writeErrorTrace()

        self.setTimeEnd()
        if self.__bLogTiming:
            lstTimings = []

            dictTimeStamps["end"] = time.time()
            lstTimings.append("EDAction.executeKernel: profiling of %s %i \t total time duration = %.3f s" % (self.getClassName(), self.getId(), dictTimeStamps["end"] - dictTimeStamps["init"]))
            fTimeForFailureCalculation = dictTimeStamps["init"]
            if "preProcess" in  dictTimeStamps:
                lstTimings.append("\t preProcess \t\t time duration = %.3f s" % (dictTimeStamps["preProcess"] - dictTimeStamps["init"]))
                fTimeForFailureCalculation = dictTimeStamps["preProcess"]

            if "process" in dictTimeStamps:
                lstTimings.append("\t process \t\t time duration = %.3f s" % (dictTimeStamps["process"] - dictTimeStamps["slotPreProcess"]))
                fTimeForFailureCalculation = dictTimeStamps["process"]
            if "postProcess" in dictTimeStamps:
                lstTimings.append("\t postProcess \t\t time duration = %.3f s" % (dictTimeStamps["postProcess"] - dictTimeStamps["slotProcess"]))
                fTimeForFailureCalculation = dictTimeStamps["postProcess"]
            fTimeForFinallyCalculation = fTimeForFailureCalculation
            if "slotSUCCESS" in dictTimeStamps:
                lstTimings.append("\t slotSUCCESS \t\t time duration = %.3f s" % (dictTimeStamps["slotSUCCESS"] - dictTimeStamps["slotPostProcess"]))
                fTimeForFailureCalculation = dictTimeStamps["slotSUCCESS"]
            if "slotFAILURE" in dictTimeStamps:
                lstTimings.append("\t slotFAILURE \t\t time duration = %.3f s" % (dictTimeStamps["slotFAILURE"] - fTimeForFailureCalculation))
            if dictTimeStamps.has_key("finallyProcess"):
                lstTimings.append("\t finallyProcess \t time duration = %.3f s" % (dictTimeStamps["finallyProcess"] - fTimeForFinallyCalculation))
            self.log(os.linesep.join(lstTimings))

    def synchronize(self):
        """
        Wait for the thread to finish. Since the time out is used by
        e.g. EDPluginExecProcessScript we add an extra second in order
        to allow the subclasses to handle the time out - without this
        extra second it's the EDAction class who time-outs first.
        
        Note that this does not in any case add time to the execution,
        because the extra second is only used for time-outs. The method
        returns immediately once the thread has finished.
        """
        EDVerbose.DEBUG("EDAction.synchronize() for %s" % self.getName())
#        fTimeOut = self.__fTimeOutInSeconds
        if self.__fTimeOutInSeconds is None:
            self.__fTimeOutInSeconds = self.__fDefaultTimeOutInSeconds

        #Wait for the thread to be started up to timeout
        if self.isStarted() == False:
            tStartWait = time.time()
            while self.isStarted() == False:
                time.sleep(1)
                if time.time() - tStartWait > self.__fTimeOutInSeconds:
                    self.__bIsTimeOut = True
                    strErrorMessage = "Timeout when waiting for %s to start!" % self.getClassName()
                    EDVerbose.DEBUG("EDAction.synchronize: " + strErrorMessage)
                    EDVerbose.ERROR(strErrorMessage)
                    self.setFailure()
                    return
        # We add an extra second in order to allow execution plugin to finish
        # which have the same timeout
        self.join(float(self.__fTimeOutInSeconds + 1))
        for fExtraTime in self.__lExtraTime:
            self.join(float(fExtraTime))
        if self.isAlive():
            # Timeout!
            self.__bIsTimeOut = True
            EDVerbose.DEBUG("EDAction.synchronize: Timeout!")
            strErrorMessage = "Timeout when waiting for %s to terminate." % self.getClassName()
            EDVerbose.ERROR(strErrorMessage)
            self.setFailure()


    def isTimeOut(self):
        return self.__bIsTimeOut


    def hasTimedOut(self, _bTimeout):
        """
        Enforce the timeout state
        
        @param _bTimeout: if you think you can force this !
        @type _bTimeout: boolean
        """
        self.__bIsTimeOut = bool(_bTimeout)


    def isFailure(self):
        return self.__bIsFailure


    def setFailure(self):
        self.__bIsFailure = True


    def run(self):
        self.executeKernel()


    def executeAction(self, _edObject=None):
        self.execute(_edObject)


    def executeActionSynchronous(self, _edObject=None):
        self.executeSynchronous()



    def connectPreProcess(self, _oMethod):
        self.synchronizeOn()
        if (_oMethod != None):
            self.__edSlotPreProcess.connect(_oMethod)
        self.synchronizeOff()


    def connectProcess(self, _oMethod):
        self.synchronizeOn()
        if (_oMethod != None):
            self.__edSlotProcess.connect(_oMethod)
        self.synchronizeOff()


    def connectPostProcess(self, _oMethod):
        self.synchronizeOn()
        if (_oMethod != None):
            self.__edSlotPostProcess.connect(_oMethod)
        self.synchronizeOff()


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

    def connectFinallyProcess(self, _oMethod):
        self.synchronizeOn()
        if (_oMethod != None):
            self.__edSlotFinallyProcess.connect(_oMethod)
        self.synchronizeOff()

    def isRunning(self):
        return self.isAlive()

    def isEnded(self):
        EDVerbose.DEBUG("%s.isEnded return %s" % (self.getName(), (self.getTimeEnd() is not None)))
        return (self.getTimeEnd() is not None)

    def isStarted(self):
        EDVerbose.DEBUG("%s.isStarted return %s, %s " % (self.getName(), (self.getTimeInit() is not None), self.getTimeInit()))
        return (self.getTimeInit() is not None)


    def setTimeOut(self, _fTimeOut):
        """
        Sets the time out
        """
        EDVerbose.DEBUG("EDAction.setTimeOut called with value %s" % _fTimeOut)
        self.__fTimeOutInSeconds = float(_fTimeOut)


    def getTimeOut(self):
        """
        Returns the time out
        """
        if self.__fTimeOutInSeconds is None:
            self.__fTimeOutInSeconds = self.__fDefaultTimeOutInSeconds
        return self.__fTimeOutInSeconds

    def addExtraTime(self, _fExtraTime):
        """
        Allows to incread the timeout of a plugin while it is running
        @param _fExtraTime: extra time to be added to timeout
        @type _fExtraTime: float
        """
        self.__lExtraTime.append(_fExtraTime)
        self.setTimeOut(self.getTimeOut() + _fExtraTime)

    def getDefaultTimeOut(self):
        """
        Returns the time out
        """
        return self.__fDefaultTimeOutInSeconds


    def getSlotSUCCESS(self):
        return self.__edSlotSUCCESS


    def getSlotFAILURE(self):
        return self.__edSlotFAILURE


    def preProcess(self, _edObject=None):
        pass


    def process(self, _edObject=None):
        pass


    def postProcess(self, _edObject=None):
        pass


    def abort(self, _edObject=None):
        pass


    def finallyProcess(self, _edObject=None):
        pass


    def execute(self, _edObject=None):
        self.__bIsStarted = True
        self.__edObject = _edObject
        self.start()


    def executeSynchronous(self, _edObject=None):
        self.execute(_edObject)
        self.synchronize()


    def setLogTiming(self, _bValue):
        """
        Force this action to log it's timing to file 
        """
        self.__bLogTiming = bool(_bValue)

    def getLogTiming(self):
        return self.__bLogTiming
    logTiming = property(getLogTiming, setLogTiming)

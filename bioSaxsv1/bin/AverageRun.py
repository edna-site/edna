#!/usr/bin/env python
# -*- coding: utf8 -*-
#
#    Project: BioSaxs
#             http://www.edna-site.org
#
#    File: "$Id: EDParallelExecute.py 1990 2010-08-26 09:10:15Z svensson $"
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
   
"""

__author__ = "Jérôme Kieffer"
__contact__ = "Jerome.Kieffer@ESRF.eu"
__license__ = "GPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"

import os, sys, threading, tempfile, signal, time

# Append the EDNA kernel source directory to the python path

if not os.environ.has_key("EDNA_HOME"):
    strProgramPath = os.path.abspath(sys.argv[0])
    pyListPath = strProgramPath.split(os.sep)
    if len(pyListPath) > 3:
        strEdnaHomePath = os.sep.join(pyListPath[:-3])
    else:
        print ("Problem in the EDNA_HOME path ..." + strEdnaHomePath)
        sys.exit()
    os.environ["EDNA_HOME"] = strEdnaHomePath

sys.path.append(os.path.join(os.environ["EDNA_HOME"], "kernel", "src"))

from EDVerbose          import EDVerbose
from EDFactoryPlugin    import EDFactoryPlugin
from EDUtilsParallel    import EDUtilsParallel


#As an example, you can define the plugin name here
EDNAPluginName = "EDPluginBioSaxsAveragev1_0"

#Here we defile three functions for managing XML strings
def fnXMLinExample(_listStrFilename):
    """
    Here we create the XML string to be passed to the EDNA plugin from the input _strFilename
    This can / should be modified by the final user
    
    @param _strFilename: full path of the input file
    @type _strFilename: python string representing the path
    @rtype: XML string
    @return: python string  
    """
    prefix = os.path.commonprefix(_listStrFilename)
    listFilesReversed = []
    for oneFile in _listStrFilename:
        revLst = list(oneFile)
        revLst.reverse()
        listFilesReversed.append("".join(revLst))
    revLst = list(os.path.commonprefix(listFilesReversed))
    revLst.reverse()
    suffix = "".join(revLst)
    averagedImage = prefix + "ave" + suffix
    base = os.path.splitext(averagedImage)[0]
    averagedCurve = base + ".dat"
    logFile = base + ".log"
    xml = "<XSDataInput>\
<integratedImageSize><value>26000</value></integratedImageSize>" + \
" ".join(["<integratedImage><path><value>%s</value></path></integratedImage>" % i for i in _listStrFilename]) + \
"<averagedCurve><path><value>%s</value></path></averagedCurve>\
<averagedImage><path><value>%s</value></path></averagedImage>\
<logFile><path><value>%s</value></path></logFile>\
</XSDataInput>" % (averagedCurve, averagedImage, logFile)
    return xml


def fnXMLoutExample(_strXMLin, _strXMLout):
    """
    This is an example of XMLout function ... it prints only the name of the file created
    @param srXMLin: The XML string used to launch the job
    @type _strXMLin: python string with the input XML
    @param _strXMLout: The XML string retrieved  job
    @type _strXMLout: python string with the output XML    
    @rtype: None
    @return: None     
    """
    print "Successful processing of :"
    print _strXMLin
    print _strXMLout
    return None


def fnXMLerrExample(_strXMLin):
    """
    This is an example of XMLerr function ... it prints only the name of the file created
    @param _strXMLin: The XML string used to launch the job
    @type _strXMLin: python string with the input XML
    @rtype: None
    @return: None     
    """
    print "An error occurred while proceeding this :"
    print _strXMLin
    return None



class EDParallelExecute:
    """ 
    A class helping to make a multi-threaded application from a plugin name and a list of files. 
    """
    __edFactoryPlugin = EDFactoryPlugin()

    def __init__(self, _strPluginName, _functXMLin, \
                  _functXMLout=None, _functXMLerr=None, \
                  _iNbThreads=None, _fDelay=1.0, _bVerbose=None, _bDebug=None):
        """
        This is the constructor of the edna plugin launcher.
        
        @param _strPluginName: the name of the ENDA plugin
        @type  _strPluginName: python string
        
        @param _functXMLin: a function taking a path in input and returning the XML string for input in the EDNA plugin. 
        @type  _functXMLin: python function
        
        @param _functXMLOut: a function to be called each time a plugin gas finished his job sucessfully, it should take two option: strXMLin an strXMLout
        @type  _functXMLOut: python function
         
        @param _functXMLErr: a function to be called each time a plugin gas finished his job and crashed, it should take ONE option: strXMLin
        @type  _functXMLErr: python function 
        
        @param _iNbThreads: The number of parallel threads to be used by EDNA, usually the number of Cores of the computer. If 0 or None, the number of cores  will be auto-detected. 
        @type  _iNbThreads: python integer
        
        @param _fDelay: The delay in seconds between two directories analysis 
        @type  _fDelay: python float
        
        @param _bVerbose:  Do you want the EDNA plugin execution to be verbose ?
        @type  _bVerbose: boolean

        @param _bDebug:  Do you want EDNA plugin execution debug output (OBS! very verbose) ?
        @type  _bDebug: boolean
        """

        self.__iNbThreads = EDUtilsParallel.detectNumberOfCPUs(_iNbThreads)
        EDUtilsParallel.initializeNbThread(self.__iNbThreads)
        self.__semaphoreOut = threading.Semaphore()
        self.__semaphoreErr = threading.Semaphore()
        self.__strPluginName = _strPluginName
        self.__functXMLin = _functXMLin
        self.__functXMLout = _functXMLout
        self.__functXMLerr = _functXMLerr
        self.__strCurrWorkDir = os.getcwd()
        self.__strTempDir = None
        self.__listInputPaths = []
        if _bVerbose is not None:
            if _bVerbose:
                EDVerbose.setVerboseDebugOn()
            else:
                EDVerbose.setVerboseOff()
        if _bDebug is not None:
            if _bDebug:
                EDVerbose.setVerboseDebugOn()
            else:
                EDVerbose.setVerboseDebugOff()
        self.__fDelay = _fDelay #default delay between two directory checks.
        self.__bQuit = False    # To check if we should quit the application
        self.__bIsFirstExecute = True
        signal.signal(signal.SIGTERM, self.handleKill)
        signal.signal(signal.SIGINT, self.handleKill)


    def runEDNA(self, _pyListInputPaths=[ "." ], _strMode="dirwatch", _bNewerOnly=False):
        """
        This method runs the parallel execution on the list of directories.

        @param _pyListInputPaths: the name of the directories to look after.
        @type  _pyListInputPaths: python list of strings
        
        @param _strMode: can be dirwatch, inotify, or OffLine (inotify being not yet implemented)
        @type _strMode: python string

        @param _bNewerOnly: in online mode, process only new files (appearing after the program has started), by default it will process all files then wait for newer files and process them.
        @type _bNewerOnly: boolean
        """
        self.moveToTempDir()
        self.__listInputPaths = _pyListInputPaths
#        if _strMode == "dirwatch":
#            self.watch_directories(_bNewerOnly)
#        elif _strMode == "inotify":
#            print "inotify online notify mode not yet implemented"
#            raise
#        else: #mode offline
        self.runEdnaFunction(self.__listInputPaths, _bIncludeSubdirs=True)
        self.waitForAllProcessToFinish()


    def moveToTempDir(self):
        """
        Create a temporary directory and put all logs there
        """
        self.__strCurrWorkDir = os.getcwd()
        self.__strTempDir = tempfile.mkdtemp(suffix='.log', prefix='edna-')
        EDVerbose.screen("The log directory of EDNA will be in " + self.__strTempDir)
        os.chdir(self.__strTempDir)


    def start(self, _strXmlInput):
        """
        Launch EDNA with the given XML stream
        @param _strXmlInput:  XML to be passed to the plugin
        @type  _strXmlInput: python string representing the XML data structure
        """
        if (_strXmlInput is None) or (_strXmlInput == "") :
            return
        #This is a trick to work-around bug #463:
        #  Run the fist thread alone (delay the second, third, ...)
        #    semaphore._Semaphore__value is the current value of the value, unfortunatly it is a protected value without getter 
        #    I need the value of the semaphore to guess if the current call is the first or not.
        #    Nota semaphore are decreased in value from self.__iNbThreads to 0. When Zero, the semaphore is blocking.
        # Them all other, limited by the semaphore.

        if self.__bIsFirstExecute:
            sys.stdout.write("Waiting for first thread to initialize ....")
            while EDUtilsParallel.getNbRunning() > 0:
                time.sleep(0.5)
                sys.stdout.write(".")
        EDUtilsParallel.semaphoreNbThreadsAcquire()

        edPlugin = EDParallelExecute.__edFactoryPlugin.loadPlugin(self.__strPluginName)

        if (edPlugin is not None):

            edPlugin.setDataInput(_strXmlInput)
            edPlugin.connectSUCCESS(self.successPluginExecution)
            edPlugin.connectFAILURE(self.failurePluginExecution)
            edPlugin.execute()
            #edPlugin.executeSynchronous()
        else:
            EDUtilsParallel.semaphoreNbThreadsRelease()
            self.__bIsFirstExecute = False
            EDVerbose.screen("ERROR! Plugin not found : " + self.__strPluginName)


    def runEdnaFunction(self, _listNewFiles, _bIncludeSubdirs=False):
        """
        This method is the launcher for new files found by watch_directories ; it is also called directly in offline mode.
        
        @param  _listNewFiles: list of files newly created in the directory.
        @type   _listNewFiles: python list of strings.
        @param  _bIncludeSubdirs: should we include sub-directories ? yes for offline and no for online.
        @type   _bIncludeSubdirs: boolean
        """
        dictListFiles = {}
        for oneFile in _listNewFiles:
            if os.path.isfile(oneFile):
                if self.__bQuit == True:
                    return
                base = list(os.path.splitext(oneFile)[0])
                base.reverse()
                for i in xrange(len(base)):
                    if not base[i].isdigit():
                        break
                base = base[i:]
                base.reverse()
                base = "".join(base)

                if base in dictListFiles:
                    dictListFiles[base].append(oneFile)
                else:
                    dictListFiles[base] = [oneFile]
        for key in dictListFiles:
            EDVerbose.screen ("Processing %s: %s" % (key, dictListFiles[key]))
            self.start(self.__functXMLin(dictListFiles[key]))


    def successPluginExecution(self, _edObject=None):
        """
        Method called when the execution of the plugin succeeds 
        """
        EDUtilsParallel.semaphoreNbThreadsRelease()
        self.__bIsFirstExecute = False
        if self.__functXMLout is None:
            EDVerbose.screen("Plugin %s execution ended with success" % self.__strPluginName)
        else:
            self.__semaphoreOut.acquire()
            self.__functXMLout(_edObject.dataInput.marshal(), _edObject.getDataOutput().marshal())
            self.__semaphoreOut.release()


    def failurePluginExecution(self, _edObject=None):
        """
        Method called when the execution of the plugin failed 
        """
        EDUtilsParallel.semaphoreNbThreadsRelease()
        self.__bIsFirstExecute = False
        if self.__functXMLerr is None:
            EDVerbose.screen("Plugin %s execution ended with failure" % self.__strPluginName)
        else:
            self.__semaphoreErr.acquire()
            self.__functXMLerr(_edObject.dataInput.marshal())
            self.__semaphoreErr.release()


    def unlockErrFunction(self):
        """Method to unlock the semaphore that controls the call of an external procedure (procedure called in case of error in the EDNA pipeline)"""
        self.__semaphoreErr.release()


    def unlockOutFunction(self):
        """Method to unlock the semaphore that controls the call of an external procedure (procedure called in case of success of  EDNA pipeline)"""
        self.__semaphoreOut.release()


    def lockErrFunction(self):
        """Method to lock the semaphore that controls the call of an external procedure (procedure called in case of error in the EDNA pipeline)"""
        self.__semaphoreErr.acquire()


    def lockOutFunction(self):
        """Method to lock the semaphore that controls the call of an external procedure (procedure called in case of success of the EDNA pipeline)"""
        self.__semaphoreOut.acquire()


    def semaphoreNbThreadsAcquire(self):
        """Method to acquire the semaphore that controls the number of threads running concurrently"""
        EDUtilsParallel.semaphoreNbThreadsAcquire()


    def semaphoreNbThreadsRelease(self):
        """Method to release the semaphore that controls the number of threads running concurrently"""
        EDUtilsParallel.semaphoreNbThreadsRelease()


    def handleKill(self, signum, frame):
        """ 
        This method is launched when the program catches ctrl-c or get killed. It initialize the exit of the program
        """
        self.__bQuit = True
        sys.stderr.write("Exit requested by signal %s with frame %s.\n" % (signum, frame))
        self.waitForAllProcessToFinish()
        os.chdir(self.__strCurrWorkDir)


    def flush(self):
        """
        This method calls the functXMLin a few times with a flush=True argument or without arguments and finishes the work 
        """
        bFinished = False
        while not bFinished:
            xml = None

            try:
                xml = self.__functXMLin(None, flush=True)
            except TypeError:
                try:
                    xml = self.__functXMLin("", flush=True)
                except TypeError:
                    try:
                        xml = self.__functXMLin("")
                    except TypeError:
                        try:
                            xml = self.__functXMLin("")
                        except TypeError:
                            xml = None
        if (xml is None) or (xml == ""):
            bFinished = True
        else:
            EDVerbose.screen ("Flushing data ...")
            self.start(xml)


    def waitForAllProcessToFinish(self):
        """
        as it names says, this method waits for all plug-ins which are currently running to finish before returning.
        """
        sys.stderr.write("Waiting for launched jobs to finish .")
        while (EDUtilsParallel.getNbRunning() > 0):
            time.sleep(1)
            sys.stderr.write(".")
        sys.stderr.write("Done.\n")


    def cleanUp(self, listMethods=[]):
        """
        Final hook if you need to execute something after all processes finished (like killAllWorkers in SPD) 
        @param listMethods: allows to finish some things in the plugin. 
        @type listMethods: list of strings representing names of methods of the plugin to be called.
        """
        self.waitForAllProcessToFinish()
        edPlugin = EDParallelExecute.__edFactoryPlugin.loadPlugin(self.__strPluginName)
        for strOneMethod in  listMethods:
            try:
                print "calling edPlugin.%s" % strOneMethod
                exec "edPlugin.%s" % strOneMethod
            except Exception:
                print "error in processing " + strOneMethod

################################################################################
# END of class EDParallelExecute
################################################################################

if __name__ == '__main__':
    cwd = os.getcwd()
    listPaths = []
    strMode = "OffLine"
    bDebug = False
    bVerbose = True
    iNbCPU = None
    for strArg in sys.argv[1:]:
        strarg = strArg.lower()
#        if strarg.find("-online") in [0, 1]:
#            strMode = "dirwatch"
#        if strarg.find("-all") in [0, 1]:
#            bNewerOnly = False
#        if strarg.lower().find("-verbose") in [0, 1]:
#            bVerbose = True
        if strarg.lower().find("-debug") in [0, 1]:
            bDebug = True
        elif strarg.lower().find("-ncpu") in [0, 1]:
            try:
                iNbCPU = int(strarg.split("=", 1)[1])
            except ValueError:
                iNbCPU = None
        if os.path.exists(strArg):
            if os.path.isdir(strArg):
                for onfile in os.listdir(strArg):
                    listPaths.append(os.path.abspath(os.path.join(strArg, onfile)))
            else:
                listPaths.append(os.path.abspath(strArg))

    if len(listPaths) == 0:
        print "This is the bioSaxs application of EDNA %s, \nplease give a path to process offline or the option:\n\
        --online to process online incoming data in the given directory.\n\
        --all to process all existing files (unless they will be excluded)\n\
        --debug to turn on debugging mode in EDNA\n\
        --nCPU=xxx to specify the number of CPUs to use. Usually EDNA auto-detects the number of processors." % EDNAPluginName
        sys.exit()

    edna = EDParallelExecute(_strPluginName=EDNAPluginName, _functXMLin=fnXMLinExample, _functXMLerr=fnXMLerrExample, _bVerbose=bVerbose, _bDebug=bDebug, _iNbThreads=iNbCPU)
    edna.runEDNA(listPaths, strMode)

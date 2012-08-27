#!/usr/bin/env python
# -*- coding: utf8 -*-
#
#    Project: EDNA-Kernel
#             http://www.edna-site.org
#
#    File: "$Id$"
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
from __future__ import with_statement
__doc__ = """
This is an example on how to make a multi-threaded application processing all 
files in a set of directories, either online of offline, using an existing plugin.

This is done in 3 steps:

1. Create a function transforming the path of a filename to an XML string compatible
with the datamodel (XSDataInput) of the plugin. Input and output path can be managed there 
as well as options for the plugin.   
   
2. Instanciate EDParallelExecute with the name of the plugin and the name of the function

3. Call the runEDNA method with the name of the directories and on/offline parameters 
  
4 (optional) Call the cleanUp method for finishing some tasks
   
"""

__author__ = "Jérôme Kieffer"
__contact__ = "Jerome.Kieffer@ESRF.eu"
__license__ = "LGPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"
__status__ = "production"
__date__ = "20110921"

import os, sys, tempfile, signal, time

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

from EDLogging              import EDLogging
from EDUtilsParallel        import EDUtilsParallel
from EDJob                  import EDJob
from EDThreading            import Semaphore


#As an example, you can define the plugin name here
EDNAPluginName = "EDPluginExecThumbnailv10"

#Here we defile three functions for managing XML strings
def fnXMLinExample(_strFilename):
    """
    Here we create the XML string to be passed to the EDNA plugin from the input _strFilename
    This can / should be modified by the final user
    
    @param _strFilename: full path of the input file
    @type _strFilename: python string representing the path
    @rtype: XML string
    @return: python string  
    """
    if _strFilename.endswith(".jpg"):
        return "<XSDataInputExecCommandLine></XSDataInputExecCommandLine> "
    upperDir = os.path.dirname(os.path.dirname(_strFilename))
    if not os.path.isdir(os.path.join(upperDir, "Thumbnail")):
        os.makedirs(os.path.join(upperDir, "Thumbnail"), int("775", 8))
    destinationPath = os.path.join(upperDir, "Thumbnail")

    xml = "<XSDataInputThumbnail>\
    <inputImagePath>\
        <path>\
            <value>%s</value>\
        </path>\
    </inputImagePath>\
    <outputPath>\
        <path><value>%s</value></path></outputPath>\
    <levelsGamma>\
        <value>0.2</value></levelsGamma>\
    <levelsColorize>\
        <value>1</value></levelsColorize>\
    <thumbWidth>\
        <value>512</value>\
    </thumbWidth>\
    </XSDataInputThumbnail>" % (_strFilename, destinationPath)
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



class EDParallelExecute(EDLogging):
    """ 
    A class helping to make a multi-threaded application from a plugin name and a list of files. 
    """

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
        EDLogging.__init__(self)
        self.__iNbThreads = EDUtilsParallel.detectNumberOfCPUs(_iNbThreads)
        EDUtilsParallel.initializeNbThread(self.__iNbThreads)
################################################################################
# #We are not using the one from EDUtilsParallel to leave it to control the number of  execPlugins.
################################################################################
        self.__semaphoreNbThreads = Semaphore(self.__iNbThreads)
        self.__strPluginName = _strPluginName
        self.__functXMLin = _functXMLin
        self.__functXMLout = _functXMLout
        self.__functXMLerr = _functXMLerr
        self.__strCurrWorkDir = os.getcwd()
        self.__strTempDir = None
        self.__listInputPaths = []
        self.__dictCurrentlyRunning = {}
        if _bVerbose is not None:
            if _bVerbose:
                self.setVerboseDebugOn()
            else:
                self.setVerboseOff()
        if _bDebug is not None:
            if _bDebug:
                self.setVerboseDebugOn()
            else:
                self.setVerboseDebugOff()
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
        if _strMode == "dirwatch":
            self.watch_directories(_bNewerOnly)
        elif _strMode == "inotify":
            print "inotify online notify mode not yet implemented"
            raise
        else: #mode offline
            self.runEdnaFunction(self.__listInputPaths, _bIncludeSubdirs=True)
            self.waitForAllProcessToFinish()


    def moveToTempDir(self):
        """
        Create a temporary directory and put all logs there
        """
        self.__strCurrWorkDir = os.getcwd()
        self.__strTempDir = tempfile.mkdtemp(suffix='.log', prefix='edna-')
        self.screen("The log directory of EDNA will be in " + self.__strTempDir)
        os.chdir(self.__strTempDir)


    def start(self, _strXmlInput):
        """
        Launch EDNA with the given XML stream
        @param _strXmlInput:  XML to be passed to the plugin
        @type  _strXmlInput: python string representing the XML data structure
        """
        jobid = None
        if _strXmlInput not in ["", None]:
            job = EDJob(self.__strPluginName)
            job.setDataInput(_strXmlInput)
            job.connectFAILURE(self.failureJobExecution)
            job.connectSUCCESS(self.successJobExecution)
            job.connectCallBack(self.unregisterJob)
            self.semaphoreNbThreadsAcquire()
            jobid = job.execute()
            self.DEBUG("Running Job id %s" % jobid)
            if jobid is None:
                self.semaphoreNbThreadsRelease()
        return jobid


    def successJobExecution(self, _jobId):
        """
        Method called when the execution of the plugin finishes with success

        @param  _jobId: string of type EDPluginName-number 
        """
        self.DEBUG("EDParallelExcecute.successJobExecution for %s" % _jobId)
        self.semaphoreNbThreadsRelease()
        with self.locked():
            if self.__functXMLout is not None:
                job = EDJob.getJobFromID(_jobId)
                self.__functXMLout(job.getPlugin().getDataInput(), job.getPlugin().getDataOutput())


    def failureJobExecution(self, _jobId):
        """
        Method called when the execution of the plugin finishes with failure 
        
        @param  _jobId: string of type EDPluginName-number
        """
        self.DEBUG("EDParallelExcecute.failureJobExecution for %s" % _jobId)
        self.semaphoreNbThreadsRelease()
        with self.locked():
            if self.__functXMLerr is not None:
                self.__functXMLerr(EDJob.getJobFromID(_jobId).getPlugin().getDataInput())


    def unregisterJob(self, _jobid):
        """
        remove the filename from the list of files currently under processing

        @param  _jobId: string of type EDPluginName-number          
        """
        with self.locked():
            for oneKey in self.__dictCurrentlyRunning.copy():
                if self.__dictCurrentlyRunning[oneKey] == _jobid:
                    self.__dictCurrentlyRunning.pop(oneKey)


    def runEdnaFunction(self, _listNewFiles, _bIncludeSubdirs=False):
        """
        This method is the launcher for new files found by watch_directories ; it is also called directly in offline mode.
        
        @param  _listNewFiles: list of files newly created in the directory.
        @type   _listNewFiles: python list of strings.
        @param  _bIncludeSubdirs: should we include sub-directories ? yes for offline and no for online.
        @type   _bIncludeSubdirs: boolean
        """
        for oneFile in _listNewFiles:
            if os.path.isdir(oneFile) and _bIncludeSubdirs == True:
                for root, _, onesubdirfiles in os.walk(oneFile):
                    for onesubdirfile in onesubdirfiles:
                        strFilename = os.path.abspath(os.path.join(root, onesubdirfile))
                        if self.__bQuit == True:
                            return
                        self.processOneFile(strFilename)
            elif os.path.isfile(oneFile):
                if self.__bQuit == True:
                    return
                self.processOneFile(oneFile)


    def processOneFile(self, _strFilename):
        """
        Process on file by calling subsequently the XML generator and the start method unless this file
        is already under process (can happend with the watch_directory method).

        @param  _strFilename: filename to process
        @type _strFilename: string
        """
        if _strFilename not in self.__dictCurrentlyRunning:
            with self.locked():
                self.__dictCurrentlyRunning[_strFilename] = self.__strPluginName
            strXmlData = self.__functXMLin(_strFilename)
            if strXmlData in [None, ""]:
                self.log("Not processing % s" % _strFilename)
                with self.locked():
                    self.__dictCurrentlyRunning.pop(_strFilename)
            else:
                self.screen("Processing % s" % _strFilename)
                jobid = self.start(strXmlData)
                with self.locked():
                    if jobid is None:
                        self.__dictCurrentlyRunning.pop(_strFilename)
                    else:
                        self.__dictCurrentlyRunning[_strFilename] = jobid

    def watch_directories (self, _bNewerOnly=False):
        """
        Continuously monitors the paths and their subdirectories
        for changes.  If any files or directories are modified,
        the callable function ( here the method self.runEdnaFunction() ) is called 
        with a list of the modified paths of both
        files and directories.  This function can return a Boolean value
        for rescanning; if it returns True, the directory tree will be
        rescanned without calling the function for any found changes.
        (This is so this function can write changes into the tree and prevent itself
        from being immediately called again.)

        @param _bNewerOnly : Do you want to process only newer files  
        @type _bNewerOnly  : Boolean

        Basic principle: pyDictAllFiles is a dictionary mapping paths to
        modification times.  We repeatedly crawl through the directory
        tree rooted at 'path', doing a stat() on each file and comparing
        the modification time.

        """
        dictAllFiles = {}
        dictRemainingFiles = {}
        listChangedFiles = []

        def internalUpdateDict (unused, dirname, files):
            "Traversal function for directories"
            for strFilename in files:
                path = os.path.join(dirname, strFilename)

                try:
                    tempStat = os.stat(path)
                except os.error:
                    # If a file has been deleted between os.path.walk()
                    # scanning the directory and now, we'll get an
                    # os.error here.  Just ignore it -- we'll report
                    # the deletion on the next pass through the main loop.
                    continue

                mtime = dictRemainingFiles.get(path)
                if mtime is not None:
                    # Record this file as having been seen
                    del dictRemainingFiles[path]
                    # File's mtime has been changed since we last looked at it.
                    if tempStat.st_mtime > mtime:
                        listChangedFiles.append(path)
                else:
                    # No recorded modification time, so it must be
                    # a brand new file.
                    listChangedFiles.append(path)

                # Record current mtime of file.
                dictAllFiles[path] = tempStat.st_mtime

        if _bNewerOnly:
            for path in self.__listInputPaths:
                os.path.walk(path, internalUpdateDict, None)

        # Main loop
        rescan = False
        while not self.__bQuit:
            listChangedFiles = []
            dictRemainingFiles = dictAllFiles.copy()
            dictAllFiles = {}
            for path in  self.__listInputPaths:
                os.path.walk(path, internalUpdateDict, None)
            #removed_list = dictRemainingFiles.keys()
            if rescan:
                rescan = False
            elif listChangedFiles:
                rescan = self.runEdnaFunction(listChangedFiles, _bIncludeSubdirs=False)
            time.sleep(self.__fDelay)
        print "Quitting the online mode."


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
            self.screen ("Flushing data ...")
            self.start(xml)


    def waitForAllProcessToFinish(self):
        """
        as it names says, this method waits for all plug-ins which are currently running to finish before returning.
        """
        self.screen("Waiting for launched jobs to finish .")
        while (self.getNbRunning() > 0):
            time.sleep(1)
            sys.stderr.write(".")
        sys.stderr.write("Done.\n")
        EDJob.stats()


    def cleanUp(self, listMethods=[]):
        """
        Final hook if you need to execute something after all processes finished (like killAllWorkers in SPD) 
        @param listMethods: allows to finish some things in the plugin. 
        @type listMethods: list of strings representing names of methods of the plugin to be called.
        """
        self.waitForAllProcessToFinish()
        for strOneMethod in  listMethods:
            try:
                print "calling edPlugin.%s" % strOneMethod
                exec "edPlugin.%s" % strOneMethod
            except Exception:
                print "error in processing %s" % strOneMethod


################################################################################
# Nota: there are 2 levels of controls for the number of thread currently running:
# * One here to limit the number of control plugin running at once
# * One on the Exec plugin level for finer grain optimisation 
################################################################################
    def semaphoreNbThreadsAcquire(self):
        """Method to acquire the semaphore that controls the number of plugins running concurrently"""
#        pass
        self.__semaphoreNbThreads.acquire()


    def semaphoreNbThreadsRelease(self):
        """Method to release the semaphore that controls the number of plugins running concurrently"""
#        pass
        self.__semaphoreNbThreads.release()


    def getNbRunning(self):
        """
        Class method:
        getter for the number of CPU-active threads running
    
        @return: the number of CPU-active threads runnings
        @rtype: integer
        """
        #return EDUtilsParallel.getNbRunning()
        return self.__iNbThreads - self.__semaphoreNbThreads._Semaphore__value

################################################################################
# END of class EDParallelExecute
################################################################################

if __name__ == '__main__':
    listPaths = []
    strMode = "OffLine"
    bNewerOnly = True
    bDebug = False
    bVerbose = False
    iNbCPU = None
    for strArg in sys.argv[1:]:
        strarg = strArg.lower()
        if strarg.find("-online") in [0, 1]:
            strMode = "dirwatch"
        elif strarg.find("-all") in [0, 1]:
            bNewerOnly = False
        elif strarg.lower().find("-verbose") in [0, 1]:
            bVerbose = True
        elif strarg.lower().find("-debug") in [0, 1]:
            bDebug = True
        elif strarg.lower().find("-ncpu") in [0, 1]:
            try:
                iNbCPU = int(strarg.split("=", 1)[1])
            except ValueError:
                iNbCPU = None
        if os.path.exists(strArg):
            listPaths.append(os.path.abspath(strArg))

    if len(listPaths) == 0:
        if strMode == "OffLine":
            print "This is the DiffractionCTv1 application of EDNA %s, \nplease give a path to process offline or the option:\n\
            --online to process online incoming data in the given directory.\n\
            --all to process all existing files (unless they will be excluded)\n\
            --debug to turn on debugging mode in EDNA\n\
            --nCPU=xxx to specify the number of CPUs to use. Usually EDNA auto-detects the number of processors." % EDNAPluginName
            sys.exit()
        else:
            listPaths = [os.getcwd()]

    edna = EDParallelExecute(_strPluginName=EDNAPluginName, _functXMLin=fnXMLinExample, _functXMLout=fnXMLoutExample, _functXMLerr=fnXMLerrExample, _bVerbose=bVerbose, _bDebug=bDebug, _iNbThreads=iNbCPU)
    edna.runEDNA(listPaths, strMode , bNewerOnly)


#!/usr/bin/env python
#-*- coding: UTF8 -*-
#
#    Project: The EDNA Kernel
#             http://www.edna-site.org
#
#    File: "$Id: DocGenerator.py 1092 2010-02-02 kieffer $"
#
#    Copyright (C) 2008-2010 European Synchrotron Radiation Facility
#                            Grenoble, France
#
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
This is the documentation generator of the EDNA projet, it relies on EpyDoc, please have a look on 
U{the epydoc homepage<http://epydoc.sourceforge.net>}
"""

__author__ = "Jérôme Kieffer"
__contact__ = "Jerome.Kieffer@esrf.eu"
__license__ = "GPLv3"
__date__ = "2011-04-13"
__copyright__ = "2011-ESRF"


#
# First locate EDNA_HOME
#

import sys, os, tempfile
cwd = os.getcwd()
pyStrProgramPath = os.path.abspath(sys.argv[0])
pyStrBinPath = os.path.split(pyStrProgramPath)[0]
pyStrKernelPath = os.path.split(pyStrBinPath)[0]
pyStrEdnaHomePath = os.path.split(pyStrKernelPath)[0]
os.environ["EDNA_HOME"] = pyStrEdnaHomePath

################################################################################
# Due to a bug in Epydoc ... it will not be runned through python but rather using the command line
################################################################################

#blacklist = ["EDPluginExecSRBRegisterv10", "EDPluginExecProcess"]
strEdnaKernel = os.path.join(pyStrEdnaHomePath, "kernel", "src")
sys.path.append(strEdnaKernel)
if not "PYTHONPATH" in os.environ:
    os.environ["PYTHONPATH"] = strEdnaKernel
else:
    os.environ["PYTHONPATH"] += strEdnaKernel
os.environ["PYTHONPATH"] += os.pathsep + os.path.join(pyStrEdnaHomePath, "kernel", "tests", "src")
os.environ["PYTHONPATH"] += os.pathsep + os.path.join(pyStrEdnaHomePath, "kernel", "tests", "testsuite")


from EDJob                  import EDJob
from EDUtilsParallel        import EDUtilsParallel
from EDVerbose              import EDVerbose
from EDFactoryPluginStatic  import EDFactoryPluginStatic
EDUtilsParallel.initializeNbThread()
EDFactoryPluginStatic.loadModule("XSDataDocumentation")
from XSDataDocumentation import XSDataString, XSDataFile, XSDataInputEpydoc, XSDataInteger
dictJobs = {}

def findPlugins(EDNAHome, EDPluginPrefix="EDPlugin", XSDataPrefix="XSData", pythonExtension=".py",):
    """
    This function is the walker that goes through all directories in EDNA_HOME directory and searches for EDNA plugins ...
    
    @param EDNAHome: the path of EDNA_HOME
    @type EDNAHome: string
    @param EDPluginPrefix: the start of the name of an EDNA Plugin
    @type EDPluginPrefix: string
    @param pythonExtension: the extension of an EDNA plugin, usually .py
    @type pythonExtension: string
    @return: to be definied but probably a dictionary with {EDPlugin: path}
    @rtype: python dictionary    
    """
    results = {}
    PythonPath = []
    for root, dirs, files in os.walk(EDNAHome):
        if '.svn' in dirs:
            dirs.remove('.svn')# don't visit SVN directories
        if 'tests' in dirs:
            dirs.remove('tests')# don't visit test directories
        if "template" in dirs:
            dirs.remove('template')# don't visit template directories
        if "src" in  dirs:
            PythonPath.append(os.path.abspath(os.path.join(EDNAHome, root, "src")))
        if files != []:
            for oneFile in files:
                if oneFile.endswith(pythonExtension):
                    if oneFile.find(EDPluginPrefix) == 0 : #here we have a plugin
                        results[os.path.splitext(oneFile)[0] ] = os.path.split(os.path.abspath(os.path.join(EDNAHome, root)))[0]
                    if oneFile.find(XSDataPrefix) == 0 : #here we have a Datamodel binding
                        PythonPath.append(os.path.abspath(os.path.join(EDNAHome, root)))
    for mydir in PythonPath:
        if not mydir in sys.path:
            sys.path.append(mydir)
            os.environ["PYTHONPATH"] += ":" + mydir
    return results


def  findProjects(EDNAHome):
    """
    This function is the walker that goes through all directories in EDNA_HOME directory and searches for EDNA projects or libraries ...
    
    @param EDNAHome: the path of the EDNA_HOME top directory
    @type EDNAHome: string
    @param EDPluginPrefix: the start of the name of an EDNA Plugin
    @type EDPluginPrefix: string
    @param pythonExtension: the extension of an EDNA plugin, usually .py
    @type pythonExtension: string
    @return: a list of RelativeProjectPath 
    @rtype: python list 
    """
    pylResults = []
    for dirname in os.listdir(EDNAHome):
        if not os.path.isdir(os.path.join(EDNAHome, dirname)):
            continue
        elif dirname in ['.svn', 'tests', 'template', "tmp", "temp", ".settings"]:
            continue
        elif dirname.find("libraries") == 0:
            for subdir in os.listdir(os.path.join(EDNAHome, dirname)):
                if subdir in ['.svn', 'tests', 'template', "tmp", "temp", ".settings"]:
                    continue
                elif os.path.isdir(os.path.join(EDNAHome, dirname, subdir)):
                    pylResults.append(os.path.join(dirname, subdir))
        else:
            pylResults.append(dirname)
    return pylResults


def findFile(pluginDir, pythonExtension=".py", excludePrefixes=["XSData", "dna_", "ALJy", "EDJob", "EDParallelExecute", "EDUtilsParallel"]):
    """
    This function is the walker that goes through all directories in plugin  directory and searches for python source files ...
    
    @param pluginDir: the path to the plugin
    @type pluginDir: string
    @param pythonExtension: the extension of an EDNA plugin, usually .py
    @type pythonExtension: string
    @param excludePrefix: prefix that will not be included in code generation, typically the XSData bindings
    @type excludePrefix: python string
    @return: list of python files
    @rtype: python list 
    
    """
    results = []
    for root, dirs, files in os.walk(pluginDir):
        if '.svn' in dirs:
            dirs.remove('.svn')# don't visit SVN directories
        if files != []:
            for oneFile in files:
                if oneFile.endswith(pythonExtension):
                    for oneExt in  excludePrefixes:
                        if oneFile.startswith(oneExt):
                            break
                    else: #this is executed only if no break was encountered
                        results.append(os.path.join(pluginDir, root, oneFile))
    return results

def rmdir(topdir, bypass=False):
    """Delete everything reachable from the directory named in "top",
    assuming there are no symbolic links.
    CAUTION:  This is dangerous!  For example, if top == '/', it
    could delete all your disk files.
    @param topdir: the directory to remove, the directory will stay there, but emptied.
    @type topdir: python string
    @param bypass: bypass the security if True
    @type  bypass: boolean
    """
    topdir = os.path.abspath(topdir)
    if not os.path.isdir(topdir):
        EDVerbose.screen("The argument topdir= %s is not a directory, giving up" % (topdir))
        return
    if ((topdir.find(pyStrEdnaHomePath) != 0) or (pyStrEdnaHomePath == topdir))and not bypass :
        EDVerbose.screen("This is a dangerous method, lets play only in sub-directories of EDNA_HOME")
        return
    for root, dirs, files in os.walk(topdir, topdown=False):
        if '.svn' in dirs:
            dirs.remove('.svn')# don't visit SVN directories
        for name in files:
            os.remove(os.path.join(root, name))
        for name in dirs:
            try:
                os.rmdir(os.path.join(root, name))
            except OSError:
                EDVerbose.screen("Error in removing: " + os.path.join(root, name))



 ###############################################################################
 # this is the main program if somebody wants to use this as a library
 ###############################################################################
if __name__ == '__main__':
    cwd = os.getcwd()
    workdir = tempfile.mkdtemp("doc", "tmp", os.getenv("HOME"))
#    if not os.path.exists(workdir):
#        os.makedirs(workdir)
    os.chdir(workdir)
    docFormat = "html"
    CleanAll = False
    WebSite = False
    bVerbose = False
    pathWebDoc = ""
    for i in sys.argv:
        if i == "--pdf":
            docFormat = "pdf "
        elif i == "--clean":
            CleanAll = True
        elif i == "--website":
            WebSite = True
        elif i == "-v":
            bVerbose = True
        elif os.path.isdir(i):
            pathWebDoc = i

    if WebSite and pathWebDoc:
        print "Generating web documentation in  ", pathWebDoc
        rmdir(pathWebDoc, bypass=True)
        for oneproject in findProjects(pyStrEdnaHomePath):
            print ("Generating HTML pages for " + oneproject)
            docPath = os.path.join(pathWebDoc, oneproject)
            os.makedirs(docPath, int("755", 8))
            listOfPythonFiles = findFile(os.path.join(pyStrEdnaHomePath, oneproject))
            listOfPythonFiles.sort()
            if len(listOfPythonFiles) > 0:
                epydocJob = EDJob("EDPluginExecEpydocv1_0")
                dictJobs[oneproject] = epydocJob
                xsd = XSDataInputEpydoc()
                xsd.setDocPath(XSDataFile(XSDataString(docPath)))
                xsd.setProjectName(XSDataString(oneproject))
                xsd.setDocType(XSDataString(docFormat))
                if bVerbose:
                    xsd.setVerbosity(XSDataInteger(1))
                else:
                    xsd.setVerbosity(XSDataInteger(-1))
                xsd.setSources([XSDataFile(XSDataString(oneFile)) for oneFile in listOfPythonFiles])
                epydocJob.setDataInput(xsd)
                epydocJob.execute()
            else:
                print ("Error: No python files for project %s" % oneproject)

    else:
        plugins = findPlugins(pyStrEdnaHomePath)
        pluginPathProcessed = []
        for oneplugin in plugins:
            pluginPath = plugins[oneplugin]
            if not pluginPath in pluginPathProcessed:
                pluginPathProcessed.append(pluginPath)
                docPath = os.path.join(pluginPath, "doc")
                if not os.path.isdir(docPath):
                    os.mkdir(docPath)
                if CleanAll:
                    rmdir(docPath)
                EDVerbose.screen("%40s --> %s" % (oneplugin, plugins[oneplugin]))
                myPluginPath = os.path.join(pluginPath, "plugins", oneplugin + ".py")
                listOfPythonFiles = []
                if os.path.isfile(myPluginPath):
                    listOfPythonFiles = [myPluginPath]
                for onePyFile in findFile(pluginPath):
                    if not onePyFile in  listOfPythonFiles:
                        listOfPythonFiles.append(onePyFile)
                if len(listOfPythonFiles) > 0:
                    epydocJob = EDJob("EDPluginExecEpydocv1_0")
                    dictJobs[oneplugin] = epydocJob
                    xsd = XSDataInputEpydoc()
                    xsd.setDocPath(XSDataFile(XSDataString(docPath)))
                    xsd.setProjectName(XSDataString(oneplugin))
                    xsd.setDocType(XSDataString(docFormat))
                    if bVerbose:
                        xsd.setVerbosity(XSDataInteger(2))
                    else:
                        xsd.setVerbosity(XSDataInteger(-1))
                    xsd.setSources([XSDataFile(XSDataString(oneFile)) for oneFile in listOfPythonFiles ])
                    epydocJob.setDataInput(xsd)
                    epydocJob.execute()
                else:
                    print ("Error: No python files for plugin %s" % oneplugin)
    EDVerbose.screen("Back to main")
    for jobName in dictJobs:
        job = dictJobs[jobName]
        if job.getStatus() in [EDJob.PLUGIN_STATE_RUNNING, EDJob.PLUGIN_STATE_UNITIALIZED]:
            EDVerbose.screen("Waiting for job %s to finish" % jobName)
            job.synchronize()
    EDVerbose.screen("Generation of documentation finished")
    os.chdir(cwd)
    EDJob.stats()

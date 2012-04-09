#!/usr/bin/env python
# -*- coding: utf8 -*-
#
#    Project: PROJECT
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) European Synchrotron Radiation Facility, Grenoble, France
#
#    Principal author:       Jerome Kieffer (Jerome.Kieffer@ESRF.eu)
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
#
#

"""EDNA external libraries builder and installer, useful for PIL, numpy, scipy, Fabio, ... """

__contact__ = "Jerome.Kieffer@ESRF.eu"
__author__ = "Jerome Kieffer"
__license__ = "GPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"

import os, shutil, sys, zipfile, tarfile, urllib2, threading
from   EDVerbose        import  EDVerbose
from EDUtilsPlatform    import EDUtilsPlatform
from EDUtilsPath        import EDUtilsPath

for strOneArg in sys.argv:
    if strOneArg.lower() in ["-d", "--debug"]:
        EDVerbose.setVerboseDebugOn()

class EDUtilsLibraryInstaller:
    """
    This class helps to install to install an external library within EDNA
    """
    iMAX_DOWNLOAD_TIME = 60 #in seconds
    def __init__(self, _strLibraryDirectory, _strArchiveName=None, _strSourceDir=None):
        """
        Constructor of the class EDUtilsLibraryInstaller,
        
        @param _strLibraryDirectory: the name of the directory where the library is, like  "20090711-SciPy-0.7.1"
        @type _strLibraryDirectory: python string
        @param _strArchiveName: the name of the archive file. if None, the system will try to guess it, searching in  _strLibraryDirectory for a tar.gz, tar.bz2 or a .zip
        @type _strArchiveName: python string
        @param _strSourceDir: the name of the directory where the setup.py file is, this could be guessed as well is None.
        @type _strSourceDir: python string
        """
        self.__strLibraryDirectory = _strLibraryDirectory
        self.__strArchiveName = _strArchiveName
        self.__strSourceDir = _strSourceDir
        self.__strDestinationDirectory = None
        if os.environ.has_key("EDNA_HOME"):
            self.__libraryPath = os.path.join(EDUtilsPath.EDNA_HOME, "libraries", self.__strLibraryDirectory)
        else:
            self.__libraryPath = os.path.dirname(os.path.abspath(sys.argv[0]))

    @staticmethod
    def checkPythonVersion():
        """
        Checks that we are using at least python2.5 as zip and tarfiles modules are required to uncompress archive
        even if those modules exists since python2.3 their API has changed in python2.5. 
        """
        if sys.version_info < (2, 5):
            raise ImportError, "Version of python too old, please use a python 2.5 or newer.\nCurrently you are using Python " + sys.version


    def dependency(self, _strLibraryName, _strLibraryDirectory, _tupleVersion=None, _strMethodToGetVersion=None):
        """Tries to resolve a dependency on an external library like numpy
        
        @param _strLibraryName: name of the library, "numpy" for example
        @type _strLibraryName: Python string
        @param _strLibraryDirectory:  the name of the directory where the dependency library is, like  "20090405-Numpy-1.3"
        @type _strLibraryDirectory: Python string
        @param _tupleVersion: the minimum version of the library to be installed. 
        @type: _tuplVersion: tuple of integer
        @param _strMethodToGetVersion: for numpy it would be "version.version"
        @type _strMethodToGetVersion: string
        """
        dictModulesBeforeImport = sys.modules.copy()
        strDepLibPath = os.path.join(os.path.dirname(self.__libraryPath), _strLibraryDirectory, EDUtilsPlatform.architecture)
        EDVerbose.DEBUG("LibInstaller.dependency: strDepLibPath=%s" % strDepLibPath)
        try:
            mylib = __import__(_strLibraryName)
        except Exception:
            if os.path.isdir(strDepLibPath)and (strDepLibPath not in sys.path):
                sys.path.insert(1, strDepLibPath)
                if os.environ.has_key("PYTHONPATH"):
                    os.environ["PYTHONPATH"] += os.pathsep + strDepLibPath
                else:
                    os.environ["PYTHONPATH"] = strDepLibPath

            else:
                installLibrary(strDepLibPath)
            mylib = __import__(_strLibraryName)

        tupleVersionObt = None
        if _strMethodToGetVersion is not None and _tupleVersion is not None:
#            mylib = __import__(_strLibraryName)
            try:
                versionObt = eval("mylib.%s" % (_strMethodToGetVersion))
            except Exception:
                EDVerbose.WARNING("Unable to execute version %s.%s" % (_strLibraryName, _strMethodToGetVersion))
                versionObt = None
            if isinstance(versionObt, (unicode, str)):
                try:
                    tupleVersionObt = tuple(map(int, versionObt.split(".")))
                except Exception:
                    EDVerbose.WARNING("Unable to understand Version %s" % versionObt)
                    versionObt = None
            elif isinstance(versionObt, tuple):
                tupleVersionObt = versionObt
            else:
                del dictModulesBeforeImport
#                EDVerbose.screen("Version of Numpy Library found: %s" % numpy.version.version)
                return
        if tupleVersionObt is not None:
            if tupleVersionObt < _tupleVersion:
                EDVerbose.WARNING("Wrong library version: %s < %s" % (tupleVersionObt, _tupleVersion))
                for oneModule in sys.modules.copy():
                    if oneModule not in dictModulesBeforeImport:
                        del sys.modules[ oneModule ]
                if os.path.isdir(strDepLibPath):# and (strDepLibPath not in sys.path):
                    sys.path.insert(1, strDepLibPath)
                    if "PYTHONPATH" in os.environ:
                        os.environ["PYTHONPATH"] = strDepLibPath + os.pathsep + os.environ["PYTHONPATH"]
                    else:
                        os.environ["PYTHONPATH"] = strDepLibPath

                else:
                    installLibrary(strDepLibPath)
                __import__(_strLibraryName)

        del dictModulesBeforeImport



    @staticmethod
    def searchCLib(_strLibName):
        """
        Search in the LD_PRELOAD, LD_LIBRARY_PATH and subsequently in /etc/ld.so.conf & /etc/ld.so.conf.d/* for a library named 
       
        @param _strLibName: name of the file or library to look for
        @type _strLibName: python string
        @return: the name of the path where the library is (or None if it was not found
        @rtype: string or None  
        """
        strLibPath = None
        listLib = []
        if "LD_PRELOAD" in os.environ:
            for oneLib in os.environ["LD_PRELOAD"].split(":"):
                if oneLib not in listLib and os.path.isdir(oneLib):
                    listLib.append(oneLib)
        if "LD_LIBRARY_PATH" in os.environ:
            for oneLib in os.environ["LD_LIBRARY_PATH"].split(":"):
                if oneLib not in listLib and os.path.isdir(oneLib):
                    listLib.append(oneLib)
        if os.path.isdir("/etc/ld.so.conf"):
            listLdSoConf = open("/etc/ld.so.conf").readlines()
            listLdSoConf.reverse()
            for oneLib in listLdSoConf:
                oneLibS = oneLib.strip()
                if oneLibS.startswith("include"):
                    includeDir = os.path.dirname(oneLibS.split()[1])
                    for strLdFile in os.listdir(includeDir):
                        confFile = os.path.join(includeDir, strLdFile)
                        for subdir in open(confFile).readlines():
                            subdirS = subdir.strip()
                            if subdirS not in listLib and os.path.isdir(oneLibS):
                                listLib.append(subdirS)
                elif oneLibS not in listLib and os.path.isdir(oneLibS):
                    listLib.append(oneLibS)
        for oneLib in ["/usr/local/lib", "/usr/lib", "/lib"]:
            if os.path.isdir(oneLib) and oneLib not in listLib:
                listLib.append(oneLib)


        for oneLib in listLib:
            for oneFile in os.listdir(oneLib):
                if oneFile.startswith(_strLibName):
                    strLibPath = oneLib
                    return strLibPath
        return strLibPath


    def getArchiveName(self):
        """
        Tries to guess the name of the archive from it's extension
        
        @return: Name of the archive
        @rtype: python string
        """
        if self.__strArchiveName == None:
            for oneFile in os.listdir(self.__libraryPath):
                if os.path.isfile(oneFile) and \
                os.path.splitext(oneFile)[1].lower() in[".gz", ".bz2", ".zip", ".tgz", ".tbz", ".tbz2"]:
                    self.__strArchiveName = oneFile
        return self.__strArchiveName

    def unZipArchive(self):
        """
        Uncompress the archived installer by using tar or zip
        """
        if self.__strArchiveName == None:
            self.getArchiveName()
        cwd = os.getcwd()
        EDVerbose.DEBUG("Unzipping archive %s in directory %s." % (self.__strArchiveName, self.__libraryPath))

        os.chdir(self.__libraryPath)
        strArchiveNameLower = self.__strArchiveName.lower()
        if strArchiveNameLower.endswith(".zip"):
            zipped = zipfile.ZipFile(self.__strArchiveName)
            if self.__strSourceDir == None:
                self.__strSourceDir = os.path.dirname(zipped.filelist[0].filename)
                if self.__strSourceDir == "":
                    self.__strSourceDir = zipped.filelist[0].filename
            zipped.extractall()
            zipped.close()
        elif strArchiveNameLower.endswith(".tgz") or strArchiveNameLower.endswith(".tar.gz") \
            or strArchiveNameLower.endswith(".tbz") or strArchiveNameLower.endswith(".tar.bz2") :
            tar = tarfile.open(self.__strArchiveName)
            if self.__strSourceDir == None:
                self.__strSourceDir = os.path.dirname(tar.getmembers()[0].name)
                if self.__strSourceDir == "":
                    self.__strSourceDir = tar.getmembers()[0].name
            tar.extractall()
            tar.close()
        os.chdir(cwd)


    def cleanSources(self):
        """
        Remove the source tree and clean up the installation directory to save some place
        """
        for root, dirs, files in os.walk(os.path.join(self.__libraryPath, self.__strSourceDir), topdown=False):
            for name in files:
                os.remove(os.path.join(root, name))
            for name in dirs:
                os.rmdir(os.path.join(root, name))
        os.rmdir(os.path.join(self.__libraryPath, self.__strSourceDir))


    def buildSources(self, _strOptions=""):
        """
        Runs the setup.py to install the program within EDNA
        
        @param _strOptions: options to be passed to setup.py (beside build)
        @type _strOptions: python string
        """
        cwd = os.getcwd()
        os.chdir(os.path.join(self.__libraryPath, self.__strSourceDir))
        sys.path = [sys.path[0], os.path.join(self.__libraryPath, self.__strSourceDir)] + sys.path[1:]
        EDVerbose.DEBUG("%s$ python setup.py build  %s " % (os.getcwd(), _strOptions))
        os.system("%s setup.py build %s 2>&1" % (sys.executable, _strOptions))
        os.chdir(cwd)


    def installGeneric(self, _strPrefix, _strStartSubDir=None):
        """
        Install/Move the source/build/prefix to the library directory
        very specific to EDNA
        @param _strPrefix: prefix of the path like "build/lib.linux-x86_64-2.5"
        @type _strPrefix: string
        @param _strStartSubDir: prefix of the path like "numpy/core/include/numpy"
        @type _strStartSubDir: string
        """
        if _strStartSubDir is None:
            if _strPrefix is None:
                build = os.path.join(self.__libraryPath, _strPrefix)
            else:
                build = os.path.join(self.__libraryPath, self.__strSourceDir, _strPrefix)
            dest = self.getDestinationDirectory()
        else:
            if _strPrefix is None:
                build = os.path.join(self.__libraryPath, self.__strSourceDir, _strStartSubDir)
            else:
                build = os.path.join(self.__libraryPath, self.__strSourceDir, _strPrefix, _strStartSubDir)
            dest = os.path.join(self.getDestinationDirectory(), _strStartSubDir)
        EDVerbose.DEBUG("Installing python library from %s to %s" % (build, dest))
        if os.path.isdir(build):
            if os.path.isdir(dest):
                EDVerbose.DEBUG("walking in %s" % build)
                for dirpath, dirnames, filenames in os.walk(build):
                    EDVerbose.DEBUG("%s, %s, %s" % (dirpath, dirnames, filenames))
                    shortdir = dirpath[len(build) + 1:]
                    for oneDir in dirnames:
                        if not os.path.isdir(os.path.join(dest, shortdir, oneDir)):
                            os.makedirs(os.path.join(dest, shortdir, oneDir))
                    for oneFile in filenames:
                        target = os.path.join(shortdir, oneFile)
#                        EDVerbose.DEBUG("target %s" % target)
                        if not os.path.isfile(os.path.join(dest, target)):
                            shutil.move(os.path.join(build, target), os.path.join(dest, target))
            else:
                EDVerbose.DEBUG("mv %s to %s" % (build, dest))
                shutil.move(build, dest)
        else:
            EDVerbose.ERROR("Error in installing the library: No %s" % build)


    def installBuilt(self):
        """
        Install/Move the source/build/arch to the library directory
        very specific to EDNA
        """
        if os.path.isdir(os.path.join(self.__libraryPath, self.__strSourceDir, "build", EDUtilsPlatform.systemArchitecture)):
            self.installGeneric(os.path.join("build", EDUtilsPlatform.systemArchitecture))
        elif os.path.isdir(os.path.join(self.__libraryPath, self.__strSourceDir, "build", "lib")):
            self.installGeneric(os.path.join("build", "lib"))


    def installSources(self):
        """
        Install/Move the source/build/src.arch to the library directory
        very specific to EDNA
        """
        self.installGeneric(os.path.join("build", "src" + EDUtilsPlatform.systemArchitecture[3:]))


    def configure(self, _strOptions=""):
        """
        Run the configure program to configure the set-up
        
        @param _strOptions: options to be passed to configure
        @type _strOptions: python string
        """
        cwd = os.getcwd()
        EDVerbose.DEBUG("dir=" + os.path.join(self.__libraryPath, self.__strSourceDir))
        os.chdir(os.path.join(self.__libraryPath, self.__strSourceDir))
        EDVerbose.DEBUG("%s$ ./configure %s" % (os.getcwd(), _strOptions))
        strOutput = os.popen("./configure  %s 2>&1" % _strOptions).read()
        EDVerbose.DEBUG(strOutput)
        os.chdir(cwd)


    def make(self, _strOptions=""):
        """
        Run the make program configure program to compile the library
        
        @param _strOptions: options to be passed to make program
        @type _strOptions: python string        
        """
        cwd = os.getcwd()
        EDVerbose.DEBUG("dir=" + os.path.join(self.__libraryPath, self.__strSourceDir))
        os.chdir(os.path.join(self.__libraryPath, self.__strSourceDir))
        EDVerbose.DEBUG("%s$ make  %s" % (os.getcwd(), _strOptions))
        strOutput = os.popen("make %s 2>&1" % (_strOptions)).read()
        EDVerbose.DEBUG(strOutput)
        os.chdir(cwd)


    def downloadLibrary(self, _strServer="http://www.edna-site.org/pub/libraries"):
        """
        Download the given library from edna-site by default or another server if provided.
        
        @param _strServer: optionally, the name of the server 
        @type _strServer:  python string
        """
        if not os.path.exists(self.__strArchiveName):
            EDVerbose.screen("Trying to download library %s, timeout set to %d s" % (self.__strArchiveName, EDUtilsLibraryInstaller.iMAX_DOWNLOAD_TIME))
            if os.environ.has_key("http_proxy"):
                dictProxies = {'http': os.environ["http_proxy"]}
                proxy_handler = urllib2.ProxyHandler(dictProxies)
                opener = urllib2.build_opener(proxy_handler).open
            else:
                opener = urllib2.urlopen
            strURL = "/".join((_strServer, self.__strArchiveName))
            # Nota: since python2.6 there is a timeout in the urllib2                    
            if sys.version > (2, 6):
                data = opener(strURL, data=None, timeout=EDUtilsLibraryInstaller.iMAX_DOWNLOAD_TIME).read()
            else: #python 2.5, we use a different thread
                timer = threading.Timer(EDUtilsLibraryInstaller.iMAX_DOWNLOAD_TIME + 1, timeoutDuringDownload)
                timer.start()
                data = opener(strURL, data=None).read()
                timer.cancel()

            try:
                open(self.__strArchiveName, "wb").write(data)
            except IOError:
                raise IOError, "unable to write downloaded data to disk at " + self.__strArchiveName

            if os.path.exists(self.__strArchiveName):
                EDVerbose.screen("Library %s successfully downloaded." % self.__strArchiveName)
            else:
                raise RuntimeError, "Could not automatically download libraries %r! \n \
                                     If you are behind a firewall, please set the environment variable http_proxy. \n \
                                     Otherwise please try to download the images manually from \n \
                                     http://www.edna-site.org/pub/libraries" % self.__strArchiveName


    def getDestinationDirectory(self):
        """
        Getter for the distinationDirectory:
        
        @return: /$EDNA_HOME/libraries/libName/lib.linux-x86_64-2.x
        @rtype: string
        """
        if self.__strDestinationDirectory is None:
            self.__strDestinationDirectory = os.path.join(self.__libraryPath, EDUtilsPlatform.architecture)
            EDVerbose.DEBUG("Setting DestinationDirectory to %s" % self.__strDestinationDirectory)
            if not os.path.isdir(self.__strDestinationDirectory):
                os.makedirs(self.__strDestinationDirectory)
        return self.__strDestinationDirectory


    def getSourceDirectory(self):
        """
        Getter for the source directory:
        
        @return: /$EDNA_HOME/libraries/libName/myLib/
        @rtype: string
        """
        return self.__strSourceDir


    def getLibraryDirectory(self):
        """
        Getter for the Libary Path:
        
        @return: ....
        @rtype: string
        """
        return self.__strLibraryDirectory


    @staticmethod
    def getArchitecture():
        """
        here only fro compatibility reason ... please use EDUtilsPlatform.architecture 
        
        @return lib.linux-i386-2.6
        @rtype: string
        """
        return EDUtilsPlatform.architecture


def timeoutDuringDownload():
    """
    Function called after a timeout in the download part ... just raise an Exception. 
    """
    raise RuntimeError("Could not automatically download library ! \n \
                         If you are behind a firewall, please set the environment variable http_proxy. \n \
                         Otherwise please try to download the images manually from \n \
                         http://www.edna-site.org/pub/libraries")


def installLibrary(_strPath):
    """
    Runs the EDNA library installer in the given directory (no dependencies inside the kernel)
    @param _strPath: full path of the diresctory where the install script is
    @type _strPath: string
    """
    EDVerbose.DEBUG("Building H5Py %s" % _strPath)
    cwd = os.getcwd()
    if _strPath in sys.path: sys.path.remove(_strPath)
    os.chdir(os.path.dirname(_strPath))
    os.system("%s install.py" % sys.executable)
    os.chdir(cwd)
    sys.path.insert(1, _strPath)

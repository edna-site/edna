# coding: utf8
#
#    Project: The EDNA Kernel
#             http://www.edna-site.org
#
#    Copyright (C) 2008-2012 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal authors: Marie-Francoise Incardona (incardon@esrf.fr)
#                       Olof Svensson (svensson@esrf.fr) 
#                       Jérôme Kieffer (jerome.kieffer@esrf.eu)
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

__authors__ = [ "Marie-Francoise Incardona", "Olof Svensson", "Jérôme Kieffer" ]
__contact__ = "svensson@esrf.fr"
__license__ = "LGPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"
__date__ = "20120216"


import os, glob, tempfile, getpass, hashlib
from EDThreading import Semaphore
from EDVerbose import EDVerbose
from os.path import dirname, abspath, exists

class classproperty(property):
    def __get__(self, obj, type_):
        return self.fget.__get__(None, type_)()
    def __set__(self, obj, value):
        cls = type(obj)
        return self.fset.__get__(None, cls)(value)


class EDUtilsPath:
    """
    This is a static utility class for handling of paths.
    """

    EDNA_HOME = dirname(dirname(dirname(abspath(__file__))))
    os.environ["EDNA_HOME"] = EDNA_HOME
    _EDNA_SITE = None
    _EDNA_USERTEMPFOLDER = None
    _EDNA_TESTIMAGES = None
    _EDNA_TESTS = None
    _EDNA_TESTDATA = None
    _USER = os.getenv("USER", "UndefindedUser")
    _TMPDIR = os.getenv("TMPDIR", tempfile.gettempdir())

    _EDNA_PROJECTS = {} # key: project name. Value: path to the project root
    _EDNA_PLUGINCACHE = None

    __semaphore = Semaphore()


    @classmethod
    def appendListOfPaths(cls, _strPath, _listOfPaths):
        """
        Appends a list of paths to a path, for example [ "..", "..", "..", "..", "src" ],
        and returns the absolute path.
        """

        return abspath(os.path.join(_strPath, * _listOfPaths))


    @classmethod
    def mergePath(cls, _strPath1, _strPath2):
        """
        Merges two paths and returns the absolute path.
        Deprecated: please use 'os.path.join' instead
        """
        EDVerbose.log("EDUtilsPath.mergePath is deprecated, please use 'os.path.join' instead")
        strNewPath = os.path.join(_strPath1, _strPath2)
        return abspath(strNewPath)


    @classmethod
    def getAbsolutePath(cls, _strPath):
        """
        Returns the absolute path.
        Deprecated: please use 'os.path.abspath' instead
        """
        EDVerbose.log("EDUtilsPath.getAbsolutePath is deprecated, please use 'os.path.abspath' instead")
        return abspath(_strPath)


    @classmethod
    def existPath(cls, _strPath):
        """
        Checks if a folder exists.
        Deprecated: please use 'os.path.exists' instead
        """
        EDVerbose.log("EDUtilsPath.existPath is deprecated, please use 'os.path.exists' instead")
        return exists(_strPath)


    @classmethod
    def getEdnaHome(cls):
        """
        Returns the EDNA_HOME variable from environment if not already defined
        """
        return cls.EDNA_HOME


    @classmethod
    def setEdnaHome(cls, _strEdnaHome):
        """
        Sets EDNA_HOME home
        """
        cls.EDNA_HOME = _strEdnaHome


    @classmethod
    def getEdnaSite(cls):
        """
        Returns the EDNA_SITE variable from environment
        """
        # EDNA Site
        if(cls._EDNA_SITE == None):
            cls._EDNA_SITE = os.environ.get("EDNA_SITE")
            if(cls._EDNA_SITE is None):
                EDVerbose.warning("EDUtilsPath.getEdnaSite: EDNA_SITE not set, using EDNA_SITE='default'")
                cls._EDNA_SITE = "default"
            else:
                EDVerbose.DEBUG("EDUtilsPath.getEdnaSite: EDNA_SITE is set: %s" % cls._EDNA_SITE)
        return cls._EDNA_SITE


    @classmethod
    def setEdnaSite(cls, _strEdnaSite):
        """
        Sets EDNA_SITE
        """
        cls._EDNA_SITE = _strEdnaSite
    EDNA_SITE = classproperty(getEdnaSite, setEdnaSite)

    @classmethod
    def getCwd(cls):
        """
        Returns the current directory.
        Deprecated: please use 'os.getcwd' instead
        """
        EDVerbose.log("EDUtilsPath.getCwd is deprecated, please use 'os.getcwd' instead")
        return os.getcwd()


    @classmethod
    def createFolder(cls, _strFolderName):
        """
        Creates a folder (directory) if it doesn't already exists.
        This used to be deprecated but IS neverthless thread safe (see bug#681)
        """
        EDVerbose.log("EDUtilsPath.createFolder: %s" % _strFolderName)
        with cls.__semaphore:
            if (not exists(_strFolderName)):
                os.makedirs(_strFolderName)


    @classmethod
    def getFileList(cls, _strPath="./", _strMask="*"):
        """
        Returns a list of file and directory names given a path to a directory.
        """
        if _strMask == "*":
            listFile = os.listdir(_strPath)
        else:
            strFind = os.path.join(_strPath, _strMask)
            listPath = glob.glob(strFind)
            listFile = []
            for strPath in listPath:
                strPath = os.path.basename(strPath)
                listFile.append(strPath)
        return listFile


    @classmethod
    def getFolderName(cls, _str):
        """
        Returns the name of a folder (directory) for a given path.
        Deprecated: please use 'os.path.dirname' instead
        """
        return dirname(_str)


    @classmethod
    def getEdnaUserTempFolder(cls):
        """
        Returns the name of a temporary folder that is unique for a given user.
        """
        if cls._EDNA_USERTEMPFOLDER is None:
            if os.environ.has_key("EDNA_USERTEMPFOLDER"):
                cls._EDNA_USERTEMPFOLDER = os.environ["EDNA_USERTEMPFOLDER"]
                if not os.path.exists(cls._EDNA_USERTEMPFOLDER):
                    EDVerbose.warning("EDNA_USERTEMPFOLDER environment variable is set to %s put the directory does not exist!" % cls._EDNA_USERTEMPFOLDER)
                    cls._EDNA_USERTEMPFOLDER = None
                elif (not os.access(cls._EDNA_USERTEMPFOLDER, os.W_OK)):
                    EDVerbose.warning("EDNA_USERTEMPFOLDER environment variable is set to %s put the directory cannot be accessed!" % cls._EDNA_USERTEMPFOLDER)
                    cls._EDNA_USERTEMPFOLDER = None
            if cls._EDNA_USERTEMPFOLDER is None:
                strEdnaTempFileDir = tempfile.gettempdir()
                try:
                    # Working on Windows and Linux:
                    strUserName = getpass.getuser()
                except Exception:
                    # Working on MacOS:
                    strUserName = os.getlogin()
                bIsOk = False
                # Check that we have write access to this directory:
                if os.access(strEdnaTempFileDir, os.W_OK) and os.access(strEdnaTempFileDir, os.X_OK):
                    cls._EDNA_USERTEMPFOLDER = os.path.join(strEdnaTempFileDir, "edna-%s" % strUserName)
                    # Check that we have write access to this directory:
                    if not os.path.exists(cls._EDNA_USERTEMPFOLDER):
                        try:
                            os.mkdir(cls._EDNA_USERTEMPFOLDER)
                        except Exception:
                            EDVerbose.WARNING("Error when trying to create the directory %s" % cls._EDNA_USERTEMPFOLDER)
                    if os.access(cls._EDNA_USERTEMPFOLDER, os.W_OK) and os.access(cls._EDNA_USERTEMPFOLDER, os.X_OK):
                        bIsOk = True
                if not bIsOk:
                    # We cannot use the edna-<user name> folder... 
                    EDVerbose.WARNING("EDUtilsFile.getEdnaUserTempFolder: cannot access user temporary directory %s" % cls._EDNA_USERTEMPFOLDER)
                    # Create temporary directory
                    cls._EDNA_USERTEMPFOLDER = tempfile.mkdtemp(prefix="edna-")
                    EDVerbose.WARNING("Created temporary directory for this session: %s" % cls._EDNA_USERTEMPFOLDER)
                    EDVerbose.WARNING("If you would like to continue to use this directory for future sessions")
                    EDVerbose.WARNING("please set then environment variable EDNA_USERTEMPFOLDER to %s" % cls._EDNA_USERTEMPFOLDER)
        return cls._EDNA_USERTEMPFOLDER


    @classmethod
    def getEdnaPluginCachePath(cls):
        """This private method initializes the path to the plugin cache file"""
        if cls._EDNA_PLUGINCACHE is None:
            if "EDNA_PLUGINCACHE" in os.environ.keys():
                cls._EDNA_PLUGINCACHE = os.environ["EDNA_PLUGINCACHE"]
                strDirName = os.path.dirname(cls._EDNA_PLUGINCACHE)
                if os.path.exists(cls._EDNA_PLUGINCACHE) and (not os.access(cls._EDNA_PLUGINCACHE, os.W_OK)):
                    EDVerbose.warning("EDNA_PLUGINCACHE environment variable is set to %s but the file is not writeable!" % cls._EDNA_PLUGINCACHE)
                    cls._EDNA_PLUGINCACHE = None
                elif not os.path.exists(strDirName):
                    EDVerbose.warning("EDNA_PLUGINCACHE environment variable is set to %s put the parent directory does not exist!" % cls._EDNA_PLUGINCACHE)
                    cls._EDNA_PLUGINCACHE = None
                elif not os.access(strDirName, os.W_OK):
                    EDVerbose.warning("EDNA_PLUGINCACHE environment variable is set to %s put the parent directory cannot be accessed!" % cls._EDNA_PLUGINCACHE)
                    cls._EDNA_PLUGINCACHE = None
            if cls._EDNA_PLUGINCACHE is None:
                strTempFileDir = EDUtilsPath.getEdnaUserTempFolder()
                # We create a hash of the path in order to be able to reference several different EDNA_HOME 
                # caches in the same directory
                strCacheFileName = hashlib.sha1(os.getenv('EDNA_HOME')).hexdigest() + ".xml"
                cls._EDNA_PLUGINCACHE = os.path.abspath(os.path.join(strTempFileDir, strCacheFileName))
            EDVerbose.DEBUG("EDFactoryPlugin: Path to plugin cache: %s" % cls._EDNA_PLUGINCACHE)
        return cls._EDNA_PLUGINCACHE

    @classmethod
    def getEdnaTestPath(cls):
        """
        This class method initializes the path to the test path (probably unused)
        """
        if cls._EDNA_TESTS is None:
            if "EDNA_TESTS" in os.environ.keys():
                cls.setEdnaTestDataPath(os.environ["EDNA_TESTS"])
            if cls._EDNA_TESTS is None:
                cls._EDNA_TESTS = os.path.join(cls.EDNA_HOME, "tests",)
            EDVerbose.DEBUG("EDFactoryPlugin: Path to Test Data directory : %s" % cls._EDNA_TESTS)
        return cls._EDNA_TESTS

    @classmethod
    def setEdnaTestPath(cls, value):
        """
        This class method initializes the path to the test data (probably unused)
        """
        cls._EDNA_TESTS = os.path.abspath(value)
        if not os.path.isdir(cls._EDNA_TESTS):
            EDVerbose.warning("EDNA_TESTS environment variable is set to %s put the directory does not exist!" % cls._EDNA_TESTS)
            cls._EDNA_TESTS = None
    EDNA_TESTS = classproperty(getEdnaTestPath, setEdnaTestPath)


    @classmethod
    def getEdnaTestDataPath(cls):
        """
        This class method initializes the path to the test data (probably unused)
        """
        if cls._EDNA_TESTDATA is None:
            if "EDNA_TESTDATA" in os.environ.keys():
                cls.setEdnaTestDataPath(os.environ["EDNA_TESTDATA"])
            if cls._EDNA_TESTDATA is None:
                cls._EDNA_TESTDATA = os.path.join(cls.EDNA_HOME, "tests", "data")
            EDVerbose.DEBUG("EDFactoryPlugin: Path to Test Data directory : %s" % cls._EDNA_TESTDATA)
        return cls._EDNA_TESTDATA

    @classmethod
    def setEdnaTestDataPath(cls, value):
        """
        This class method initializes the path to the test data (probably unused)
        """
        cls._EDNA_TESTDATA = os.path.abspath(value)
        if not os.path.isdir(cls._EDNA_TESTDATA):
            EDVerbose.warning("EDNA_TESTDATA environment variable is set to %s put the directory does not exist!" % cls._EDNA_TESTDATA)
            cls._EDNA_TESTDATA = None
    EDNA_TESTDATA = classproperty(getEdnaTestDataPath, setEdnaTestDataPath)


    @classmethod
    def getEdnaTestDataImagesPath(cls):
        """
        This class method initializes the path to the test images downloaded from internet
        """
        if cls._EDNA_TESTIMAGES is None:
            if "EDNA_TESTIMAGES" in os.environ.keys():
                cls.setEdnaTestDataImagesPath(os.environ["EDNA_TESTIMAGES"])
            if cls._EDNA_TESTIMAGES is None:
                cls._EDNA_TESTIMAGES = os.path.join(cls.EDNA_HOME, "tests", "data", "images")
            EDVerbose.DEBUG("EDFactoryPlugin: Path to Temporary Images directory : %s" % cls._EDNA_TESTIMAGES)
        return cls._EDNA_TESTIMAGES

    @classmethod
    def setEdnaTestDataImagesPath(cls, value):
        """
        This class method initializes the path to the test images downloaded from internet
        """
        cls._EDNA_TESTIMAGES = os.path.abspath(value)
        if os.path.exists(cls._EDNA_TESTIMAGES) and (not os.access(cls._EDNA_TESTIMAGES, os.W_OK)):
            EDVerbose.warning("EDNA_TESTIMAGES environment variable is set to %s but the file is not writeable!" % cls._EDNA_TESTIMAGES)
            cls._EDNA_TESTIMAGES = None
        elif not os.path.exists(cls._EDNA_TESTIMAGES):
            EDVerbose.warning("EDNA_TESTIMAGES environment variable is set to %s put the directory does not exist!" % cls._EDNA_TESTIMAGES)
            cls._EDNA_TESTIMAGES = None
        elif not os.access(cls._EDNA_TESTIMAGES, os.W_OK):
            EDVerbose.warning("EDNA_TESTIMAGES environment variable is set to %s put the directory cannot be accessed!" % cls._EDNA_TESTIMAGES)
            cls._EDNA_TESTIMAGES = None
    EDNA_TESTIMAGES = classproperty(getEdnaTestDataImagesPath, setEdnaTestDataImagesPath)

    @classmethod
    def getDictOfPaths(cls):
        """
        Return an os.environ like dict enriched with internal path 
        """
        res = {"${EDNA_HOME}": cls.EDNA_HOME,
               "${EDNA_SITE}": cls.EDNA_SITE,
               "${EDNA_TESTS}": cls.EDNA_TESTS,
               "${EDNA_TESTDATA}": cls.EDNA_TESTDATA,
               "${EDNA_TESTIMAGES}": cls.EDNA_TESTIMAGES,
               "${USER}": cls._USER,
               "${TMPDIR}": cls._TMPDIR
               }
        return res

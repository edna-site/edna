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

__authors__ = [ "Marie-Francoise Incardona", "Olof Svensson", "Jérôme Kieffer" ]
__contact__ = "svensson@esrf.fr"
__license__ = "LGPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"


import os, glob, threading
from EDVerbose import EDVerbose


class EDUtilsPath:
    """
    This is a static utility class for handling of paths.
    """

    __EDNA_HOME = None
    __EDNA_SITE = None
    __semaphore = threading.Semaphore()


    @staticmethod
    def appendListOfPaths(_strPath, _listOfPaths):
        """
        Appends a list of paths to a path, for example [ "..", "..", "..", "..", "src" ],
        and returns the absolute path.
        """
        strNewPath = _strPath
        for strPath in _listOfPaths:
            strNewPath = os.path.join(strNewPath, strPath)
        return os.path.abspath(strNewPath)


    @staticmethod
    def mergePath(_strPath1, _strPath2):
        """
        Merges two paths and returns the absolute path.
        Deprecated: please use 'os.path.join' instead
        """
        EDVerbose.DEBUG("EDUtilsPath.mergePath is deprecated, please use 'os.path.join' instead")
        strNewPath = os.path.join(_strPath1, _strPath2)
        return os.path.abspath(strNewPath)


    @staticmethod
    def getAbsolutePath(_strPath):
        """
        Returns the absolute path.
        Deprecated: please use 'os.path.abspath' instead
        """
        EDVerbose.DEBUG("EDUtilsPath.getAbsolutePath is deprecated, please use 'os.path.abspath' instead")
        return os.path.abspath(_strPath)


    @staticmethod
    def existPath(_strPath):
        """
        Checks if a folder exists.
        Deprecated: please use 'os.path.exists' instead
        """
        EDVerbose.DEBUG("EDUtilsPath.existPath is deprecated, please use 'os.path.exists' instead")
        return os.path.exists(_strPath)


    @staticmethod
    def getEdnaHome():
        """
        Returns the EDNA_HOME variable from environment if not already defined
        """
        # EDNA Home
        if EDUtilsPath.__EDNA_HOME == None:
            strEdnaHome = os.environ.get("EDNA_HOME")
            if(strEdnaHome is None):
                EDVerbose.error(" *** EDNA_HOME environment variable not defined.")
            else:
                EDUtilsPath.__EDNA_HOME = os.path.abspath(strEdnaHome)
                EDVerbose.DEBUG("EDUtilsPath.getEdnaHome: EDNA_HOME: " + EDUtilsPath.__EDNA_HOME)
                if not os.path.exists(EDUtilsPath.__EDNA_HOME):
                    EDVerbose.error("EDNA_HOME directory not found : %s" % EDUtilsPath.__EDNA_HOME)
        # Raise an error exception in case EDNA_HOME is not defined - normally this should never happen
        if (EDUtilsPath.__EDNA_HOME is None):
            strErrorMessage = "FATAL ERROR: EDNA_HOME is not defined."
            EDVerbose.error(strErrorMessage)
            raise RuntimeError, strErrorMessage
        return EDUtilsPath.__EDNA_HOME


    @staticmethod
    def setEdnaHome(_strEdnaHome):
        """
        Sets EDNA_HOME home
        """
        EDUtilsPath.__EDNA_HOME = _strEdnaHome


    @staticmethod
    def getEdnaSite():
        """
        Returns the EDNA_SITE variable from environment
        """
        # EDNA Site
        if(EDUtilsPath.__EDNA_SITE == None):
            EDUtilsPath.__EDNA_SITE = os.environ.get("EDNA_SITE")
            if(EDUtilsPath.__EDNA_SITE is None):
                EDVerbose.warning("EDUtilsPath.getEdnaSite: EDNA_SITE not set, using EDNA_SITE='default'")
                EDUtilsPath.__EDNA_SITE = "default"
            else:
                EDVerbose.DEBUG("EDUtilsPath.getEdnaSite: EDNA_SITE is set: " + EDUtilsPath.__EDNA_SITE)
        return EDUtilsPath.__EDNA_SITE


    @staticmethod
    def setEdnaSite(_strEdnaSite):
        """
        Sets EDNA_SITE
        """
        EDUtilsPath.__EDNA_SITE = _strEdnaSite


    @staticmethod
    def getCwd():
        """
        Returns the current directory.
        Deprecated: please use 'os.getcwd' instead
        """
        EDVerbose.DEBUG("EDUtilsPath.getCwd is deprecated, please use 'os.getcwd' instead")
        return os.getcwd()


    @staticmethod
    def createFolder(_strFolderName):
        """
        Creates a folder (directory) if it doesn't already exists.
        This used to be deprecated but IS neverthless thread safe (see bug#681)
        """
        EDVerbose.DEBUG("EDUtilsPath.createFolder: %s" % _strFolderName)
        EDUtilsPath.__semaphore.acquire()
        if (not os.path.exists(_strFolderName)):
            os.makedirs(_strFolderName)
        EDUtilsPath.__semaphore.release()


    @staticmethod
    def getFileList(_strPath="./", _strMask="*"):
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


    @staticmethod
    def getFolderName(_str):
        """
        Returns the name of a folder (directory) for a given path.
        Deprecated: please use 'os.path.dirname' instead
        """
        #EDVerbose.DEBUG( "EDUtilsPath.getFolderName is deprecated, please use 'os.path.dirname' instead" )
        return os.path.dirname(_str)



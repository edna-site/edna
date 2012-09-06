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
__doc__ = """
This is a static utility class for handling of files.
"""


import os, shutil
from EDVerbose import EDVerbose


class EDUtilsFile(object):

    
    @staticmethod
    def readFile(_strFileName):
        """
        Reads and returns the content of a file.
        @param _strFileName: Path to the file
        @return: String containing the contents of the file.
        """
        strContent = None
        try:
            strContent = open(_strFileName, "rb").read()
        except Exception, e:
            strError = "EDUtilsFile.readFile: Reading %s: %s" % (_strFileName, str(e))
            EDVerbose.ERROR(strError)
            raise IOError(strError)
        return strContent


    @staticmethod
    def writeFile(_strFileName, _strContent):
        """
        Writes a string to a file. If the string is not already in unicode
        format it will be converted to unicode.
        @param _strFileName: Path to file, will be created if not existing
        @param _strContent: String content to be written to the file
        """
        try:
            with open(_strFileName, "wb") as myFile:
                if type(_strContent) == unicode:
                    myFile.write(_strContent)
                else:
                    myFile.write(unicode(_strContent, errors='ignore'))
                myFile.flush()
        except Exception, e:
            strError = "EDUtilsFile.writeFile: Writing %s: %s" % (_strFileName, str(e))
            EDVerbose.ERROR(strError)
            raise IOError(strError)


    @classmethod
    def readFileAndParseVariables(cls, _strFileName, _dict=None):
        """
        Returns the content of this file as a string.
        Any environment variables present in the file are substituted, as well as
        any occurrences of strings in the optional dictionary.
        @param _strFileName: Path to the file
        @param _dict: Optional dictoionary
        """
        strContent = cls.readFile(_strFileName)
        # Substitute environment variables 
        strContent = os.path.expandvars(strContent)
        if (_dict is not None):
            for key in _dict.keys():
                try:
                    strContent = strContent.replace(key , _dict[ key ])
                except Exception:
                    EDVerbose.ERROR("%s: %s" % (key , _dict[ key ]))
        return strContent

    @staticmethod
    def getFileExtension(_strFileName):
        """
        Returns the file extension, e.g. "img" for "testscale_1_001.img"
        @param _strFileName: String containing the file name
        """
        strFileExtension = None
        strFileSplit = os.path.splitext(_strFileName)
        if (len(strFileSplit) > 1):
            strExtensionWithSeparator = strFileSplit[1]
            if (len(strExtensionWithSeparator) > 1):
                # Remove the separator
                strFileExtension = strExtensionWithSeparator[1:]
        return strFileExtension

    @staticmethod
    def getBaseName(_strFileName):
        return os.path.basename(_strFileName)

    @staticmethod
    def copyFile(_strSource, _strDestination):
        shutil.copyfile(_strSource, _strDestination)

    @staticmethod
    def deleteFile(_strFileName):
        if (_strFileName is not None):
            if (os.path.exists(_strFileName)):
                os.remove(_strFileName)


# coding: utf8
#
#    Project: The EDNA Kernel
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2008 European Synchrotron Radiation Facility
#                       Grenoble, France
#
#    Principal authors: Marie-Francoise Incardona (incardon@esrf.fr)
#                       Olof Svensson (svensson@esrf.fr) 
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

__authors__ = [ "Olof Svensson", "Marie-Francoise Incardona", "Jérôme Kieffer" ]
__contact__ = "svensson@esrf.fr"
__license__ = "LGPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"
__date__ = "20120213"

from EDUtilsPath            import EDUtilsPath
from EDUtilsFile            import EDUtilsFile
from EDFactoryPluginTest    import EDFactoryPluginTest
from EDDecorator            import deprecated


class EDUtilsTest:

    __edFactoryPluginTest = None

    @classmethod
    def getFactoryPluginTest(cls):
        if (cls.__edFactoryPluginTest is None):
            cls.__edFactoryPluginTest = EDFactoryPluginTest()
        return cls.__edFactoryPluginTest


    @staticmethod
    def readAndParseFile(_strFileName):
        """
        Reads a file and parses potential existing environment variables such as:
         - EDNA_TESTS_DATA_HOME
        Returns the content of this file as a string
        """
        return EDUtilsFile.readFileAndParseVariables(_strFileName, EDUtilsPath.getDictOfPaths())


    @staticmethod
    @deprecated
    def readFileAndParseVariable(_strFileName, _strKey, _strValue):
        """
        Reads a file and parses potential existing environment variables such as:
        Returns the content of this file as a string
        """

        return EDUtilsFile.readFileAndParseVariables(_strFileName, {_strKey:_strValue})


    @staticmethod
    @deprecated
    def readFileAndParseVariables(_strFileName, _dictReplacements):
        """
        Returns the content of this file as a string
        """
        return EDUtilsFile.readFileAndParseVariables(_strFileName, _dictReplacements)


    @staticmethod
    @deprecated
    def readFile(_strFileName):
        """
        Reads a file
        Returns its content as a string
        """
        return EDUtilsFile.readFile(_strFileName)

    @staticmethod
    @deprecated
    def writeFile(_strFileName, _strContent):
        """
        Writes a string into a file
        """
        EDUtilsFile.writeFile(_strFileName, _strContent)



    @staticmethod
    @deprecated
    def getTestsHome():
        """
        Returns the tests home directory path <EDNA_HOME>/tests
        """
        return  EDUtilsPath.EDNA_TESTS


    @staticmethod
    @deprecated
    def getTestsDataHome():
        """
        Returns the tests data directory path <EDNA_HOME>/tests/data
        """
        return EDUtilsPath.EDNA_TESTDATA


    @staticmethod
    @deprecated
    def getTestsDataImagesHome():
        """
        Returns the tests data image directory path <EDNA_HOME>/tests/data/images or what is relevant
        """
        return EDUtilsPath.EDNA_TESTIMAGES


    @classmethod
    def getPluginTestDataDirectory(cls, _strPluginTestName):
        """
        Given a test case name, returns the corresponding test data directory.
        """
        strModuleLocation = cls.getFactoryPluginTest().getModuleLocation(_strPluginTestName)
        strPluginTestDataDirectory = EDUtilsPath.appendListOfPaths(strModuleLocation, [ "..", "data" ])
        return strPluginTestDataDirectory


    @classmethod
    def getConfigurationHome(cls, _strPluginTestName):
        """
        Returns the configuration directory path for a given test module
        """
        strModuleLocation = cls.getFactoryPluginTest().getModuleLocation(_strPluginTestName)
        strConfigurationHome = EDUtilsPath.appendListOfPaths(strModuleLocation, [ "..", "..", "..", "..", "conf" ])
        return strConfigurationHome


    @staticmethod
    def patchMethodName(_strText):
        """
        Try to get the method name ... by first converting it to a string an processing the string ... not optimal but it works
        
        Nota: Refactored as a static method, 20100430 JKR
        
        @param _strText: anything that could be converted to string, here it seems to be a method or a function  
        @return: the word after the
        @rtype: string 
        """
        strReturn = "None Object"
        listWords = str(_strText).replace("<", " ").split()
        if "method" in listWords:
            i = listWords.index("method")
            if i < len(listWords) - 1:
                strReturn = listWords[i + 1]
        return strReturn



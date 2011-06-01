#
#    Project: The EDNA Kernel
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2008-2009 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal author: Karl Levik (karl.levik@diamond.ac.uk)
#
#    Contributing author: Olof Svensson (svensson@esrf.fr)
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

__author__ = "Karl Levik"
__contact__ = "karl.levik@diamnd.ac.uk"
__license__ = "LGPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"

import shlex

class EDCommandLine:
    """
    Base class for command line objects.
    """

    def __init__(self, _strCommandLineArgument=None):
        self.__strCommand = None
        self.__listCommandLineArgument = []
        if (isinstance(_strCommandLineArgument, str)):
            self.__strCommand = _strCommandLineArgument
            self.__listCommandLineArgument = shlex.split(self.__strCommand)
        elif (isinstance(_strCommandLineArgument, list)):
            self.__listCommandLineArgument = []
            for cmdkey in _strCommandLineArgument:
                self.__listCommandLineArgument.append(cmdkey)


    def getCommandLine(self):
        if (self.__listCommandLineArgument != None):
            self.__strCommand = ""
            for cmdkey in self.__listCommandLineArgument:
                self.__strCommand += cmdkey + " "
        return self.__strCommand


    def getCommandLineArguments(self):
        return self.__listCommandLineArgument


    def existCommand(self, _str):
        return _str in self.__listCommandLineArgument


    def getArgument(self, _str):
        for i in range(0, len(self.__listCommandLineArgument)):
            strArgument = self.__listCommandLineArgument[i]
            if (strArgument == _str):
                j = i + 1
                if j < len(self.__listCommandLineArgument):
                    return self.__listCommandLineArgument[j]
        return None


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
#                       Jerome Kieffer
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
This is a static utility class for handling of files.
"""

__authors__ = [ "Marie-Francoise Incardona", "Olof Svensson", "Jerome Kieffer" ]
__contact__ = "svensson@esrf.fr"
__license__ = "LGPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"


import os, re


class EDUtilsImage:


    @staticmethod
    def __compileAndMatchRegexpTemplate(_strPathToImage):
        listResult = []
        pyStrBaseImageName = os.path.basename(_strPathToImage)
        pyRegexp = re.compile(r'(.*)([^0^1^2^3^4^5^6^7^8^9])([0-9]*)\.(.*)')
        pyMatch = pyRegexp.match(pyStrBaseImageName)
        if (pyMatch != None):
            listResult = [ pyMatch.group(0), pyMatch.group(1) , pyMatch.group(2) , pyMatch.group(3) , pyMatch.group(4)  ]
        return listResult


    @staticmethod
    def getImageNumber(_strPathToImage):
        iImageNumber = None
        listResult = EDUtilsImage.__compileAndMatchRegexpTemplate(_strPathToImage)
        if (listResult != None):
            iImageNumber = int(listResult[3])
        return iImageNumber


    @staticmethod
    def getTemplate(_strPathToImage, _strSymbol="#"):
        strTemplate = None
        listResult = EDUtilsImage.__compileAndMatchRegexpTemplate(_strPathToImage)
        if (listResult != None):
            strPrefix = listResult[1]
            strSeparator = listResult[2]
            strImageNumber = listResult[3]
            strSuffix = listResult[4]
            strHashes = ""
            for i in range(len(strImageNumber)):
                strHashes += _strSymbol
            strTemplate = strPrefix + strSeparator + strHashes + "." + strSuffix
        return strTemplate


    @staticmethod
    def getPrefix(_strPathToImage):
        strPrefix = None
        listResult = EDUtilsImage.__compileAndMatchRegexpTemplate(_strPathToImage)
        if (listResult != None):
            strPrefix = listResult[1]
        return strPrefix


    @staticmethod
    def getSuffix(_strPathToImage):
        strSuffix = None
        listResult = EDUtilsImage.__compileAndMatchRegexpTemplate(_strPathToImage)
        if (listResult != None):
            strSuffix = listResult[4]
        return strSuffix



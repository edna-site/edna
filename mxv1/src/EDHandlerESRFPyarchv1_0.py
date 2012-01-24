#
#    Project: EDNA MXv1
#             http://www.edna-site.org
#
#    Copyright (C) 2012      European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal authors:      Olof Svensson (svensson@esrf.fr) 
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


__authors__ = [ "Olof Svensson" ]
__contact__ = "svensson@esrf.fr"
__license__ = "GPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"

import os, shutil

from EDVerbose import EDVerbose    
    
class EDHandlerESRFPyarchv1_0:

    
    @staticmethod
    def createPyarchFilePath(_strESRFPath):
        """
        This method translates from an ESRF "visitor" path to a "pyarch" path:
        /data/visitor/mx415/id14eh1/20100209 -> /data/pyarch/id14eh1/mx415/20100209
        """
        strPyarchDNAFilePath = None
        listOfDirectories = _strESRFPath.split(os.sep)
        listBeamlines = ["id14eh1", "id14eh2", "id14eh3", "id14eh4", "id23eh1", "id23eh2", "id29"]
        # Check that we have at least four levels of directories:
        if (len(listOfDirectories) > 4):
            strDataDirectory = listOfDirectories[ 1 ]
            strSecondDirectory = listOfDirectories[ 2 ]
            strProposal = None
            strBeamline = None
            if ((strDataDirectory == "data") and (strSecondDirectory == "visitor")):
                strProposal = listOfDirectories[ 3 ]
                strBeamline = listOfDirectories[ 4 ]
            elif ((strDataDirectory == "data") and (strSecondDirectory in listBeamlines)):
                strBeamline = strSecondDirectory
                strProposal = listOfDirectories[ 4 ]
            if (strProposal != None) and (strBeamline != None):
                strPyarchDNAFilePath = os.path.join(os.sep, "data")
                strPyarchDNAFilePath = os.path.join(strPyarchDNAFilePath, "pyarch")
                strPyarchDNAFilePath = os.path.join(strPyarchDNAFilePath, strBeamline)
                strPyarchDNAFilePath = os.path.join(strPyarchDNAFilePath, strProposal)
                for strDirectory in listOfDirectories[ 5: ]:
                    strPyarchDNAFilePath = os.path.join(strPyarchDNAFilePath, strDirectory)
        if (strPyarchDNAFilePath is None):
            EDVerbose.WARNING("EDHandlerESRFPyarchv1_0.createPyArchFilePath: path not converted for pyarch: %s " % _strESRFPath)
        return strPyarchDNAFilePath


    def createPyarchHtmlDirectoryPath(self, _xsDataResultCharacterisation):
        """
        This method creates a directory path for pyarch: in the same directory were the 
        images are located a new directory is created with the following convention:
        
          edna_html_prefix_runNumber
        
        """
        # First extract all reference image directory paths and names
        xsDataCollection = _xsDataResultCharacterisation.getDataCollection()
        listImageDirectoryPath = []
        listImagePrefix = []
        for xsDataSubWedge in xsDataCollection.getSubWedge():
            for xsDataImage in xsDataSubWedge.getImage():
                strImagePath = xsDataImage.getPath().getValue()
                listImageDirectoryPath.append(os.path.dirname(strImagePath))
                listImagePrefix.append(EDUtilsImage.getPrefix(strImagePath))
        # TODO: Check that all paths and prefixes are the same
        strImageDirectory = listImageDirectoryPath[0]
        strPrefix = listImagePrefix[0]
        # Remove any "ref-" or "postref-" from the prefix in order to make it fully
        # compatitble with DNA standards:
        if (strPrefix is not None):
            if (strPrefix.startswith("ref-")):
                strPrefix = strPrefix[4:]
            elif (strPrefix.startswith("postref-")):
                strPrefix = strPrefix[8:]
        strHtmlDirectoryPath = os.path.join(strImageDirectory, "edna_html_%s" % strPrefix)
        strPyarchHtmlDirectoryPath = EDHandlerESRFPyarchv1_0.createPyarchFilePath(strHtmlDirectoryPath)
        if not os.path.exists(strPyarchHtmlDirectoryPath):
            try:
                os.mkdir(strPyarchHtmlDirectoryPath)
            except:
                EDVerbose.WARNING("EDHandlerESRFPyarchv1_0.createPyarchHtmlDirectoryPath: cannot create pyarch html directory %s" % strPyarchHtmlDirectoryPath)
                strPyarchHtmlDirectoryPath = None
        return strPyarchHtmlDirectoryPath
    

    @staticmethod
    def copyHTMLFilesAndDir(_strPathToPyarchDirectory, _strPathToHTMLFile, _strPathToHTMLDir):
        if not os.path.exists(_strPathToHTMLFile):
            EDVerbose.ERROR("EDHandlerESRFPyarchv1_0.copyHTMLFilesAndDir: path to pyarch directory does not exist: %s" % _strPathToPyarchDirectory)
        elif not os.path.exists(_strPathToHTMLFile):
            EDVerbose.ERROR("EDHandlerESRFPyarchv1_0.copyHTMLFilesAndDir: path to html file does not exist: %s" % _strPathToHTMLFile)
        elif not os.path.exists(_strPathToHTMLDir):
            EDVerbose.ERROR("EDHandlerESRFPyarchv1_0.copyHTMLFilesAndDir: path to html directory does not exist: %s" % _strPathToHTMLDir)            
        else:
            try:
                strPathToPyArchHtmlDirectory = os.path.join(_strPathToPyarchDirectory, "html")
                if not os.path.exists(strPathToPyArchHtmlDirectory):
                    os.mkdir(strPathToPyArchIndexDirectory)
                shutil.copy(_strPathToHTMLFile, os.path.join(strPathToPyArchIndexDirectory, "index.html"))
                shutil.copytree(_strPathToHTMLDir, strPathToPyArchHtmlDirectory)
            except Exception, e:
                EDVerbose.ERROR("EDHandlerESRFPyarchv1_0.copyHTMLFilesAndDir: Exception caught: %r" % e)


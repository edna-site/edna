#!/usr/bin/env python
# -*- coding: utf8 -*-
#
#    Project: MXv1
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) European Synchrotron Radiation Facility, Grenoble, France
#
#    Principal author:       Olof Svensson (svensson@esrf.fr)
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

__author__ = "Olof Svensson"
__contact__ = "svensson@esrf.eu"
__license__ = "GPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"

import os, sys, tempfile, threading

def usage():
    print """This program executes EDNA MXv1 characterisation in parallel for a given directory.
    
Usage: %s path_to_image_directory

Optional arguments:

--maxExpTime     : Max exposure time per data collection [s] (Input to BEST) 
--resultFileName : Name of the result file (default "screeningResult.txt" in current working directory)
--online         : Automatic processing online of incoming data in the given directory.
--all            : Processing of all existing files (otherwise pre-existing files will be excluded)
--verbose        : Turn on verbose output from EDNA characterisation
--debug          : Turn on debugging mode in EDNA
--ncpu           : Forcing the number of parallel executions (otherwise determined by the number of processors)

""" % os.path.basename(sys.argv[0])

strCurrentDirectory = os.getcwd()


# Append the EDNA kernel source directory to the python path

strProgramPath = os.path.abspath(sys.argv[0])
pyListPath = strProgramPath.split(os.sep)
if len(pyListPath) > 3:
    strEdnaHomePath = os.sep.join(pyListPath[:-3])
else:
    print ("Problem in the EDNA_HOME path ..." + strEdnaHomePath)
    sys.exit()
os.environ["EDNA_HOME"] = strEdnaHomePath

sys.path.append(os.path.join(os.environ["EDNA_HOME"], "kernel", "src"))

from EDParallelExecute import EDParallelExecute
from EDVerbose import EDVerbose
from EDFactoryPluginStatic import EDFactoryPluginStatic

from XSDataCommon import XSDataDouble
from XSDataCommon import XSDataString
from XSDataCommon import XSDataFile
from XSDataCommon import XSDataTime

EDFactoryPluginStatic.loadModule("XSDataMXv1")
from XSDataMXv1 import XSDataDiffractionPlan
from XSDataMXv1 import XSDataResultCharacterisation

EDFactoryPluginStatic.loadModule("XSDataInterfacev1_2")
from XSDataInterfacev1_2 import XSDataInputInterface
from XSDataInterfacev1_2 import XSDataResultInterface

class EDParallelExecuteMXv1Characterisation(EDParallelExecute):

    m_strResultFileName = None
    m_fMaxExposureTime = None
    m_writeFileSemaphore = threading.Semaphore()


#As an example, you can define the plugin name here
EDNAPluginName = "EDPluginControlInterfacev1_2"

#Here we defile three functions for managing XML strings
def functionXMLin(_strFilename):
    """Here we create the XML string to be passed to the EDNA plugin from the input strFilename
    This can / should be modified by the final user
    
    @param _strFilename: full path of the input file
    @type _strFilename: python string representing the path
    @return: string  
    """
    EDVerbose.screen("Starting processing of image %s" % (_strFilename))
    # First check if the filename end with .img or .mccd:
    strXML = None
    if (_strFilename.endswith(".img") or _strFilename.endswith(".mccd") or _strFilename.endswith(".cbf")):
        xsDataInputInterface = XSDataInputInterface()
        xsDataDiffractionPlan = XSDataDiffractionPlan()
        xsDataDiffractionPlan.setMaxExposureTimePerDataCollection(XSDataTime(EDParallelExecuteMXv1Characterisation.m_fMaxExposureTime))
        xsDataInputInterface.setDiffractionPlan(xsDataDiffractionPlan)
        xsDataFile = XSDataFile()
        xsDataFile.setPath(XSDataString(_strFilename))
        xsDataInputInterface.addImagePath(xsDataFile)
        strXML = xsDataInputInterface.marshal()
    else:
        EDVerbose.screen("File name not ending with .img or .mccd - ignored : %s" % _strFilename)
    return strXML

def functionXMLout(_strXMLin, _strXMLout):
    """
    This is an example of XMLout function ... it prints only the name of the file created
    @param _srXMLin: The XML string used to launch the job
    @type _strXMLin: python string with the input XML
    @param _strXMLout: The XML string retrieved  job
    @type _strXMLout: python string with the output XML    
    @return: None     
    """
    xsDataInputInterface = XSDataInputInterface.parseString(_strXMLin)
    strImagePath = xsDataInputInterface.getImagePath()[0].getPath().getValue()
    EDVerbose.screen("Successful processing of image %s" % strImagePath)
    strResultText = os.path.dirname(strImagePath) + " " + os.path.basename(strImagePath) + " "
    xsDataResultInterface = XSDataResultInterface.parseString(_strXMLout)
    xsDataResultCharacterisation = xsDataResultInterface.getResultCharacterisation()
    # 
    xsDataIndexingResult = xsDataResultCharacterisation.getIndexingResult()
    #strResultText = _strDirectoryVisit + " " + strFileName + " "
    if (xsDataIndexingResult is None):
        strResultText += "Indexing failed"
    else:
        xsDataSelectedSolution = xsDataIndexingResult.getSelectedSolution()
        fMosaicityEstimation = xsDataSelectedSolution.getCrystal().getMosaicity().getValue()
        strResultText += "Mosaicity: %.2f " % fMosaicityEstimation
        xsDataStrategyResult = xsDataResultCharacterisation.getStrategyResult()
        if (xsDataStrategyResult is None):
            strResultText += "No strategy result"
        else:
            xsDataCollectionPlan = xsDataStrategyResult.getCollectionPlan()[0]
            xsDataStrategySummary = xsDataCollectionPlan.getStrategySummary()
            fRankingResolution = xsDataStrategySummary.getRankingResolution().getValue()
            strResultText += "Resolution: %.2f" % fRankingResolution
    writeToResultFile(strResultText)


def writeToResultFile(_strResultText):
    EDParallelExecuteMXv1Characterisation.m_writeFileSemaphore.acquire()
    print _strResultText
    strPath = EDParallelExecuteMXv1Characterisation.m_strResultFileName
    f = open(strPath, "a")
    f.write(_strResultText + "\n")
    f.close()
    EDParallelExecuteMXv1Characterisation.m_writeFileSemaphore.release()



def functionXMLerror(_strXMLin):
    """
    @param _strXMLin: The XML string used to launch the job
    @type _strXMLin: python string with the input XML
    @return: None     
    """
    xsDataInputInterface = XSDataInputInterface.parseString(_strXMLin)
    strImagePath = xsDataInputInterface.getImagePath()[0].getPath().getValue()
    strResultText = os.path.dirname(strImagePath) + " " + os.path.basename(strImagePath) + " "
    strResultText = strResultText + "Processing failed."
    writeToResultFile(strResultText)
    return None





if __name__ == '__main__':
    listPaths = []
    strMode = "OffLine"
    bNewerOnly = True
    bDebug = False
    bVerbose = False
    iNbCPU = None
    fMaxExpTime = 10000
    strResultFileName = None
    for iIndex, strArg in enumerate(sys.argv[1:]):
        strarg = strArg.lower()
        if strarg == "--online":
            strMode = "dirwatch"
        elif strarg == "--all":
            bNewerOnly = False
        elif strarg == "--debug":
            bDebug = True
        elif strarg == "--verbose":
            bVerbose = True
        elif strarg == "--ncpu":
            iNbCPU = int(sys.argv[iIndex + 2])
        elif strarg.find("--ncpu") in [0, 1]:
            iNbCPU = int(strArg.split("=", 1)[1])
        elif strArg == "--maxExpTime":
            fMaxExpTime = float(sys.argv[iIndex + 2])
        elif strArg == "--resultFileName":
            strResultFileName = sys.argv[iIndex + 2]
        if os.path.exists(strArg):
            listPaths.append(os.path.abspath(strArg))

    if len(listPaths) == 0:
        if strMode == "OffLine":
            usage()
            sys.exit()
        else:
            listPaths = [os.getcwd()]

    if strResultFileName is None:
        strResultFileName = os.path.join(strCurrentDirectory, "screeningResult.txt")
    elif os.path.dirname(strResultFileName) == "":
        strResultFileName = os.path.join(strCurrentDirectory, strResultFileName)

    EDVerbose.screen("  Results written to : %s" % strResultFileName)

    if os.path.exists(strResultFileName):
        print "  WARNING! Results file name %s already exists!" % strResultFileName
        (strPrefix, strSuffix) = os.path.splitext(strResultFileName)
        (handle, strTmpFileName) = tempfile.mkstemp(prefix=strPrefix + "-", suffix=strSuffix)
        os.close(handle)
        print "  Existing result file renamed to: %s" % strTmpFileName
        os.rename(strResultFileName, strTmpFileName)


    EDParallelExecuteMXv1Characterisation.m_strResultFileName = strResultFileName
    EDParallelExecuteMXv1Characterisation.m_fMaxExposureTime = fMaxExpTime
    edna = EDParallelExecuteMXv1Characterisation(_strPluginName=EDNAPluginName, _functXMLin=functionXMLin, _functXMLout=functionXMLout, _functXMLerr=functionXMLerror, _bVerbose=bVerbose, _bDebug=bDebug, _iNbThreads=iNbCPU)
    edna.runEDNA(listPaths, strMode , bNewerOnly)


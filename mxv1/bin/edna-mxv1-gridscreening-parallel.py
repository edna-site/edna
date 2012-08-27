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

--onlyImageQualityIndicators : Stop the characterisation after Labelit distl.signal_strength
--onlyIntegrationWithXMLOutput : Stop the characterisation after integration and create an XML file with integrated intensities
--storeInISPyB   : Store the image quality indicators result in ISPyB 
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

from XSDataCommon import XSDataTime
from XSDataCommon import XSDataFile
from XSDataCommon import XSDataString
from XSDataCommon import XSDataBoolean

EDFactoryPluginStatic.loadModule("XSDataMXv1")
from XSDataMXv1 import XSDataDiffractionPlan

EDFactoryPluginStatic.loadModule("XSDataGridScreeningv1_0")
from XSDataGridScreeningv1_0 import XSDataInputGridScreening
from XSDataGridScreeningv1_0 import XSDataResultGridScreening


class EDParallelExecuteGridScreening(EDParallelExecute):

    strResultFileName = None
    fMaxExposureTime = None
    writeFileSemaphore = threading.Semaphore()
    bOnlyImageQualityIndicators = False
    bDoOnlyIntegrationWithXMLOutput = False
    bStoreInISPyB = False
    
    


#As an example, you can define the plugin name here
EDNAPluginName = "EDPluginControlGridScreeningv1_0"

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
        xsDataInputGridScreening = XSDataInputGridScreening()
        xsDataDiffractionPlan = XSDataDiffractionPlan()
        xsDataDiffractionPlan.setMaxExposureTimePerDataCollection(XSDataTime(EDParallelExecuteGridScreening.fMaxExposureTime))
        xsDataInputGridScreening.setDiffractionPlan(xsDataDiffractionPlan)
        xsDataFile = XSDataFile()
        xsDataFile.setPath(XSDataString(_strFilename))
        xsDataInputGridScreening.setImageFile(xsDataFile)
        if EDParallelExecuteGridScreening.bOnlyImageQualityIndicators:
            xsDataInputGridScreening.setDoOnlyImageQualityIndicators(XSDataBoolean(True))
        if EDParallelExecuteGridScreening.bStoreInISPyB:
            xsDataInputGridScreening.setStoreImageQualityIndicatorsInISPyB(XSDataBoolean(True))
        if EDParallelExecuteGridScreening.bDoOnlyIntegrationWithXMLOutput:
            xsDataInputGridScreening.setDoOnlyIntegrationWithXMLOutput(XSDataBoolean(True))
        strXML = xsDataInputGridScreening.marshal()
    else:
        EDVerbose.screen("File name not ending with .img or .mccd - ignored : %s" % _strFilename)
    return strXML

def functionXMLout(_xsDataInputGridScreening, _xsDataResultGridScreening):
    """
    This is an example of XMLout function ... it prints only the name of the file created
    @param _xsDataInputGridScreening: The object used to launch the job
    @type _xsDataInputGridScreening: XSDataInputGridScreening object
    @param _xsDataResultGridScreening: The object retrieved from the job
    @type _xsDataResultGridScreening: XSDataInputGridScreening object
    @return: None     
    """
    strImagePath = _xsDataInputGridScreening.getImageFile().getPath().getValue()
    EDVerbose.screen("Successful processing of image %s" % strImagePath)
    strResultText = None
    if EDParallelExecuteGridScreening.bDoOnlyIntegrationWithXMLOutput:
        if _xsDataResultGridScreening.getResultIntegration() is not None:
            strResultText  = "  <image>\n"
            strResultText += "    <fileName>%s</fileName>\n" % _xsDataResultGridScreening.getResultIntegration().getFileName()
            strResultText += "    <fileDirectory>%s</fileDirectory>\n" % _xsDataResultGridScreening.getResultIntegration().getFileDirectory()
            strResultText += "    <integratedData>%s</integratedData>\n" % _xsDataResultGridScreening.getResultIntegration().getIntegratedData()        
            strResultText += "  </image>"
    else:
        strResultText = "%40s  " % os.path.basename(strImagePath)
        fileNameParameters = _xsDataResultGridScreening.getFileNameParameters()
        if fileNameParameters is None:
            strResultText += "%6s%10s%10s%6s" % ("NA", "NA", "NA","NA")
        else:
            strResultText += "%6s%10s%10s%6s" % (
                            fileNameParameters.getScanId1().getValue(),
                            fileNameParameters.getMotorPosition1().getValue(),
                            fileNameParameters.getMotorPosition2().getValue(),
                            fileNameParameters.getScanId2().getValue(),
                                                    )
        imageQualityIndicators = _xsDataResultGridScreening.getImageQualityIndicators()
        if imageQualityIndicators is None:
            strResultText += "%6s%6s%6s%6s%10s" % ("NA", "NA", "NA","NA", "NA")
        else:
            strMethod1Res = "%6s" % "NA"
            if imageQualityIndicators.getMethod1Res():
                strMethod1Res = "%6.1f" % imageQualityIndicators.getMethod1Res().getValue()
            strMethod2Res = "%6s" % "NA"
            if imageQualityIndicators.getMethod2Res():
                strMethod2Res = "%6.1f" % imageQualityIndicators.getMethod2Res().getValue()
            strSpotTotal = "%6s" % "NA"
            if imageQualityIndicators.getSpotTotal():
                strSpotTotal = "%6d" % imageQualityIndicators.getSpotTotal().getValue()
            strGoodBraggCandidates = "%6s" % "NA"
            if imageQualityIndicators.getGoodBraggCandidates():
                strGoodBraggCandidates = "%6d" % imageQualityIndicators.getGoodBraggCandidates().getValue()
            strTotalIntegratedSignal = "%10s" % "NA"
            if imageQualityIndicators.getTotalIntegratedSignal():
                strTotalIntegratedSignal = "%10.0f" % imageQualityIndicators.getTotalIntegratedSignal().getValue()
            strResultText += strMethod1Res + strMethod2Res + strSpotTotal + strGoodBraggCandidates + strTotalIntegratedSignal
        if _xsDataResultGridScreening.getMosaicity() is None:
            strResultText += "%6s" % "NA"
        else:
            strResultText += "%6.1f" % _xsDataResultGridScreening.getMosaicity().getValue()
        if _xsDataResultGridScreening.getRankingResolution() is None:
            strResultText += "%6s" % "NA"
        else:
            strResultText += "%6.1f" % _xsDataResultGridScreening.getRankingResolution().getValue()
        strResultText += "  " + _xsDataResultGridScreening.getComment().getValue()
    if strResultText is not None:
        writeToResultFile(strResultText)


def writeToResultFile(_strResultText):
    EDParallelExecuteGridScreening.writeFileSemaphore.acquire()
    #print _strResultText
    strPath = EDParallelExecuteGridScreening.strResultFileName
    f = open(strPath, "a")
    f.write(_strResultText + "\n")
    f.close()
    EDParallelExecuteGridScreening.writeFileSemaphore.release()



def functionXMLerror(_strXMLin):
    """
    @param _strXMLin: The XML string used to launch the job
    @type _strXMLin: python string with the input XML
    @return: None     
    """
    xsDataInputGridScreening = XSDataInputGridScreening.parseString(_strXMLin)
    strImagePath = xsDataInputGridScreening.getImagePath()[0].getPath().getValue()
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
    bOnlyImageQualityIndicators = False
    bOnlyIntegrationWithXMLOutput = False
    bStoreInISPyB = False
    for iIndex, strArg in enumerate(sys.argv[1:]):
        strarg = strArg.lower()
        if strarg == "--online":
            strMode = "dirwatch"
        elif strarg == "--onlyimagequalityindicators":
            bOnlyImageQualityIndicators = True
        elif strarg == "--onlyintegrationwithxmloutput":
            bOnlyIntegrationWithXMLOutput = True
        elif strarg == "--storeinispyb":
            bStoreInISPyB = True
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
        if bOnlyIntegrationWithXMLOutput:
            strResultFileName = os.path.join(strCurrentDirectory, "integrationResult.xml")            
        else:
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

    EDParallelExecuteGridScreening.strResultFileName = strResultFileName

    if bOnlyIntegrationWithXMLOutput:
        strResultText = "<?xml version=\"1.0\" ?>\n"
        strResultText += "<imageset>"
        writeToResultFile(strResultText)

    EDParallelExecuteGridScreening.fMaxExposureTime = fMaxExpTime
    EDParallelExecuteGridScreening.bOnlyImageQualityIndicators = bOnlyImageQualityIndicators
    EDParallelExecuteGridScreening.bDoOnlyIntegrationWithXMLOutput = bOnlyIntegrationWithXMLOutput
    EDParallelExecuteGridScreening.bStoreInISPyB = bStoreInISPyB
    edna = EDParallelExecuteGridScreening(_strPluginName=EDNAPluginName, _functXMLin=functionXMLin, _functXMLout=functionXMLout, _functXMLerr=functionXMLerror, _bVerbose=bVerbose, _bDebug=bDebug, _iNbThreads=iNbCPU)
    edna.runEDNA(listPaths, strMode , bNewerOnly)
    if bOnlyIntegrationWithXMLOutput:
        strResultText = "</imageset>"
        writeToResultFile(strResultText)


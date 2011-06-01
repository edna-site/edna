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
#    Principal author:       Jérôme Kieffer (Jerome.Kieffer@ESRF.eu)
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
__author__ = "Jerome Kieffer"
__contact__ = "Jerome.Kieffer@ESRF.eu"
__license__ = "GPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"

import os, sys

# Append the EDNA kernel source directory to the python path

#pyStrProgramPath = os.path.abspath(sys.argv[0])
#pyLPath = pyStrProgramPath.split(os.sep)
#if len(pyLPath) > 5:
#    pyStrEdnaHomePath = os.sep.join(pyLPath[:-5])
#else:
#    print ("Problem in the EDNA_HOME path ..." + pyStrEdnaHomePath)
#    sys.exit()
pyStrEdnaHomePath = "/home/kieffer/workspace/edna"
os.environ["EDNA_HOME"] = pyStrEdnaHomePath
os.environ["EDNA_SITE"] = "ESRF"

#this is a workaround for bug #336
if not os.environ.has_key("EDNA_SITE"):
    os.environ["EDNA_SITE"] = "NotConfigured"

sys.path.append(os.path.join(pyStrEdnaHomePath, "kernel", "src"))

from EDParallelExecute import EDParallelExecute


EDNAPluginName = "EDPluginSPDCorrectv10"
CORRECTED_DIRNAME = "SPDCorrect"

dictConfig = {"beamCentreInPixelsX":1156.692,
              "beamCentreInPixelsY":1236.408,
              "bufferSizeX":2048,
              "bufferSizeY":2048,
              "pixelSizeX":0.0472244,
              "pixelSizeY":0.0468315,
              "spatialDistortionFile":"/scisoft/data/ID22-ODA/K4320T.A38pool.NoHorVerFlips.spline",
              "sampleToDetectorDistance":98.724,
              "tiltRotation":130.772,
              "angleOfTilt":0.622,
              "wavelength":0.7085,
              "outputFileType":".azim",
              "darkCurrentImageFile":"/scisoft/data/ID22-ODA/darksMED_Stack.edf",
              "flatFieldImageFile":"/scisoft/data/ID22-ODA/flatsMED_Stack.edf",
              }


def fileName2xml(filename):
    """Here we create the XML string to be passed to the EDNA plugin from the input filename
    This can / should be modified by the final user
    
    @param filename: full path of the input file
    @type filename: python string representing the path
    @rtype: XML string
    @return: python string  
    """
    xml = "<XSDataInputExecCommandLine></XSDataInputExecCommandLine> "
    strDir , baseName = os.path.split(filename)
    upperDir = os.path.dirname(strDir)
    if filename.endswith(".cor") or filename.endswith(".azim"):
        return
    destinationPath = os.path.join(upperDir, CORRECTED_DIRNAME)
    if not os.path.isdir(destinationPath):
        os.makedirs(destinationPath, int("775", 8))
    xml = "<XSDataInputSPDCorrect>\
    <beamCentreInPixelsX>        <value>%s</value>    </beamCentreInPixelsX>\
    <beamCentreInPixelsY>        <value>%s</value>     </beamCentreInPixelsY>\
    <bufferSizeX>        <value>%s</value>    </bufferSizeX>\
    <bufferSizeY>        <value>%s</value>    </bufferSizeY>\
    <pixelSizeX>        <value>%s</value>    </pixelSizeX>\
    <pixelSizeY>        <value>%s</value>    </pixelSizeY>\
    <inputFile>        <path>            <value>%s</value>        </path>    </inputFile>\
    <spatialDistortionFile>        <path>            <value>%s</value>        </path>    </spatialDistortionFile>\
    <sampleToDetectorDistance>        <value>%s</value>    </sampleToDetectorDistance>\
    <tiltRotation>        <value>%s</value>    </tiltRotation>\
    <angleOfTilt>        <value>%s</value>    </angleOfTilt>\
    <wavelength>        <value>%s</value>    </wavelength>\
    <outputFileType>        <value>%s</value>    </outputFileType>\
    <outputDir>        <path>            <value>%s</value></path></outputDir>\
    <darkCurrentImageFile>      <path>            <value>%s</value>        </path>    </darkCurrentImageFile>\
    <flatFieldImageFile>        <path>            <value>%s</value>     </path>    </flatFieldImageFile>\
    </XSDataInputSPDCorrect>" \
    % (dictConfig["beamCentreInPixelsX"], dictConfig["beamCentreInPixelsY"],
       dictConfig["bufferSizeX"], dictConfig["bufferSizeY"],
       dictConfig["pixelSizeX"], dictConfig["pixelSizeY"],
       filename, dictConfig["spatialDistortionFile"],
       dictConfig["sampleToDetectorDistance"], dictConfig["tiltRotation"],
       dictConfig["angleOfTilt"], dictConfig["wavelength"], dictConfig["outputFileType"],
       destinationPath,
       dictConfig["darkCurrentImageFile"], dictConfig["flatFieldImageFile"],
#       dictConfig["startAzimuth"], dictConfig["stopAzimuth"], dictConfig["stepAzimuth"],
       )
#    print xml
    return xml

def XMLerr(strXMLin):
    """
    This is an example of XMLerr function ... it prints only the name of the file created
    @param srXMLin: The XML string used to launch the job
    @type strXMLin: python string with the input XML
    @rtype: None
    @return: None     
    """
    print("Error in the processing of :" + strXMLin)
    return


if __name__ == '__main__':
    paths = []
    mode = "OffLine"
    newerOnly = True
    debug = False
    iNbCPU = None
    for i in sys.argv[1:]:
        if i.lower().find("-online") in [0, 1]:
            mode = "dirwatch"
        elif i.lower().find("-all") in [0, 1]:
            newerOnly = False
        elif i.lower().find("-debug") in [0, 1]:
            debug = True
        elif i.lower().find("-ncpu") in [0, 1]:
            iNbCPU = int(i.split("=", 1)[1])
        elif os.path.exists(i):
            paths.append(os.path.abspath(i))

    if len(paths) == 0:
        if mode == "OffLine":
            print "This is the SPD-Correct application of %s, \nplease give a path to process offline or the option:\n\
            --online to process online incoming data in the given directory.\n\
            --all to process all existing files (unless they will be excluded)\n\
            --debug to turn on debugging mode in EDNA\n\
            --nCPU=xxx to specify the number of CPUs to use. Usually it auto-detects the number of processors." % EDNAPluginName

            sys.exit()
        else:
            paths = [os.getcwd()]
    listKeys = dictConfig.keys()
    listKeys.sort()
    for key in listKeys:
        val = raw_input("%s [%s] ?" % (key, dictConfig[key]))
        if len(val) > 0:
            dictConfig[key] = val
    edna = EDParallelExecute(EDNAPluginName, fileName2xml, _functXMLerr=XMLerr, _bVerbose=True, _bDebug=debug, _iNbThreads=iNbCPU)
    edna.runEDNA(paths, mode , newerOnly)
    edna.cleanUp(["killAllWorkers()"])

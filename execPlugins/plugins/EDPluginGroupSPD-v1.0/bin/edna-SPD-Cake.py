#!/usr/bin/env python
# -*- coding: utf8 -*-
#
#    Project: Azimuthal integration 
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

pyStrProgramPath = os.path.abspath(sys.argv[0])
pyLPath = pyStrProgramPath.split(os.sep)
if len(pyLPath) > 5:
    pyStrEdnaHomePath = os.sep.join(pyLPath[:-5])
else:
    print ("Problem in the EDNA_HOME path ..." + pyStrEdnaHomePath)
    sys.exit()
#pyStrEdnaHomePath = "/home/kieffer/workspace/edna"
os.environ["EDNA_HOME"] = pyStrEdnaHomePath
#os.environ["EDNA_SITE"] = "ESRF"

#this is a workaround for bug #336
if not os.environ.has_key("EDNA_SITE"):
    os.environ["EDNA_SITE"] = "NotConfigured"

sys.path.append(os.path.join(pyStrEdnaHomePath, "kernel", "src"))

from EDParallelExecute import EDParallelExecute


class AzimuthalIntegrationConfig(object):
    """
# Image correction parameters
DARK CURRENT = YES
DC FILE = / mntdirect / _data_id11_inhouse / jon / july09 / align6A / align6A0000.edf
FLAT - FIELD = YES
FF FILE = / mntdirect / _data_id11_inhouse / Frelon4M / F4M_Sm_July08.edf
FF SCALE = NO
FF MULTIPLIER = 1000.000
SPATIAL DIS. = YES
SD FILE = / mntdirect / _data_id11_inhouse / Frelon4M / frelon4m.spline

# Integration parameters
START AZIMUTH = 0.0
END AZIMUTH = 359.9999824
INNER RADIUS = 32.0
OUTER RADIUS = 1086.0
SCAN TYPE = 2 - THETA
1 DEGREE AZ = NO
AZIMUTH BINS = 360
RADIAL BINS = 2048
CONSERVE INT. = NO
POLARISATION = YES
GEOMETRY COR. = YES

# Experiment geometry parameters
 = 50.0
Y - PIXEL SIZE = 50.0
DISTANCE = 136.908
 = 0.2952

# Mask and dimensions
USE MASK = NO
MASK FILE = None

# I/O parameters
input_extn = edf
saving_format = SPREAD SHEET
output_extn = spr

    dictCo = {"X-BEAM CENTRE":"fBeamCentreInPixels1",
        "Y-BEAM CENTRE":"fBeamCentreInPixels1",
        "TILT ROTATION" : "fTiltRotation",
        "DIM1_DATA":"fBufferSize1",
        "DIM1_DATA":"fBufferSize2",
        "X - PIXEL SIZE":"fPixelSize1",
        "Y - PIXEL SIZE":"fPixelSize2",

        strSpatialDistortionFile = None
        fSampleToDetectorDistance = None


        "ANGLE OF TILT":"fAngleOfTilt"
        "WAVELENGTH":"fWavelength",

        strOutputFileType = None
        strDarkCurrentImageFile = None
        strFlatFieldImageFile = None
        fStartAzimuth = None
        fStopAzimuth = None
        fStepAzimuth = None

    dictDefaultUnit = {}
        strPixelSize1Unit
        strPixelSize2Unit
        strStartAzimuthUnit
        strStopAzimuthUnit
        strStepAzimuthUnit
        strWavelengthUnit
        "ANGLE OF TILT":"deg"
        strTiltRotationUnit = None
        }
    """
    def __init__(self):
        """
        Contructor of the AzimuthalIntegration:
        A container for static parameter for azimuthal integration.
        """
        fBeamCentreInPixelsX = None
        fBeamCentreInPixelsY = None
        fBufferSizeX = None
        fBufferSizeY = None
        fPixelSizeX = None
        fPixelSizeY = None
        strPixelSizeXUnit = None
        strPixelSizeYUnit = None
        strSatialDistortionFile = None
        fSampleToDetectorDistance = None
        fTiltRotation = None
        strTiltRotationUnit = None
        fAngleOfTilt = None
        strAngleOfTiltUnit = None
        fWavelength = None
        strWavelengthUnit = None
        strOutputFileType = None
        strDarkCurrentImageFile = None
        strFlatFieldImageFile = None
        fStartAzimuth = None
        fStopAzimuth = None
        fStepAzimuth = None
        strStartAzimuthUnit = None
        strStopAzimuthUnit = None
        strStepAzimuthUnit = None

    def read(self, filename):
        """
        load a configuration file as the one produced by fi2dcake.py
        
        @param filename: Name of thw file to read
        @type filename: string
        
        """
        if not isinstance(filename, (unicode, str)):
            raise RunntimeError("The filename you provided (%s) is not a string !!!" % filename)
        if not os.path.isfile(filename):
            raise RunntimeError("No such file %s" % filename)
        for oneLine in open(filename, "rb").readlines():
            key, value = oneline.split("=", 1)
            key = key.upper()
#            TODO


EDNAPluginName = "EDPluginSPDCakev1_5"
CORRECTED_DIRNAME = "SPDCacked"
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
              "startAzimuth":0,
              "stopAzimuth":360,
              "stepAzimuth":1,

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
    xml = "<XSDataInputSPDCake>\
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
    <startAzimuth><value>%s</value></startAzimuth>\
    <stopAzimuth><value>%s</value></stopAzimuth>\
    <stepAzimuth><value>%s</value></stepAzimuth>\
    </XSDataInputSPDCake>" \
    % (dictConfig["beamCentreInPixelsX"], dictConfig["beamCentreInPixelsY"],
       dictConfig["bufferSizeX"], dictConfig["bufferSizeY"],
       dictConfig["pixelSizeX"], dictConfig["pixelSizeY"],
       filename, dictConfig["spatialDistortionFile"],
       dictConfig["sampleToDetectorDistance"], dictConfig["tiltRotation"],
       dictConfig["angleOfTilt"], dictConfig["wavelength"], dictConfig["outputFileType"],
       destinationPath,
       dictConfig["darkCurrentImageFile"], dictConfig["flatFieldImageFile"],
       dictConfig["startAzimuth"], dictConfig["stopAzimuth"], dictConfig["stepAzimuth"],
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

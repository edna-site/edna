import os, time, sys, threading, tempfile

from EDFactoryPluginStatic import EDFactoryPluginStatic
EDFactoryPluginStatic.loadModule("XSDataSPDv1_0")

from XSDataCommon import XSDataAngle
from XSDataCommon import XSDataString
from XSDataCommon import XSDataFile
from XSDataCommon import XSDataDouble
from XSDataCommon import XSDataInteger
from XSDataCommon import XSDataLength

from XSDataSPDv1_0 import XSDataInputSPDCake

#lecture

def readDataFile(strDataPath, strTestParameterFile):
    dictEDdataInput = {}
# File read 
# this file available from id11 beamline

    #strFileIn = open("XDataConfigurationInput", "r")
    strFileIn = open(strDataPath + strTestParameterFile, "r")
    print "edna is retrieving datas from file on disk"
    print strFileIn
    for linefile in strFileIn:
        strLineData = linefile

        if len(strLineData) > 1:
            """@ discard comment lines """
            if strLineData[0] <> '#' :
                """ @  discard end line carriage return"""
                strLeftarg = strLineData[:-1]

                strLeftarg = strLeftarg.split('=')

                """ @ discard argument extra-spaces """

                strLeftarg[0] = strLeftarg[0].rstrip()
                strLeftarg[0] = strLeftarg[0].lstrip()
                strLeftarg[1] = strLeftarg[1].lstrip()
                strLeftarg[1] = strLeftarg[1].rstrip()
                print strLeftarg
                """@put datas in a dictionary """
                dictEDdataInput[strLeftarg[0]] = strLeftarg[1]

    print dictEDdataInput
# close file
    strFileIn.close()
    return dictEDdataInput

#writing configuration file

def writeDataFile(self):
    dictEDdataOutput = self
    #console output for control
    print dictEDdataOutput
    #strFileOut = open("XDataConfigurationOutput", "w")
    strFileOut = open(self, "wb")
#        for linefile in (dictEDdataOutput).keys():
#        strFileOut.write(linefile+'='+dictEDdataOutput[linefile]+'\n')
#        print linefile,"=",dictEDdataOutput[linefile]
#        strFileOut.close
    # write on the file, same order than initial file
    strFileOut.write("DARK CURRENT" + "=" + dictEDdataOutput["DARK CURRENT"] + os.linesep)
    strFileOut.write("DC FILE=" + dictEDdataOutput["DC FILE"] + os.linesep)
    strFileOut.write("FLAT-FIELD=" + dictEDdataOutput["FLAT-FIELD"] + os.linesep)
    strFileOut.write("FF FILE=" + dictEDdataOutput["FF FILE"] + os.linesep)
    strFileOut.write("FF SCALE=" + dictEDdataOutput["FF SCALE"] + os.linesep)
    strFileOut.write("FF MULTIPLIER=" + dictEDdataOutput["FF MULTIPLIER"] + os.linesep)
    strFileOut.write("SPATIAL DIS.=" + dictEDdataOutput["SPATIAL DIS."] + os.linesep)
    strFileOut.write("SD FILE=" + dictEDdataOutput["SD FILE"] + os.linesep)

# Integration parameters
    strFileOut.write("START AZIMUTH=" + dictEDdataOutput["START AZIMUTH"] + os.linesep)
    strFileOut.write("END AZIMUTH=" + dictEDdataOutput["END AZIMUTH"] + os.linesep)
    strFileOut.write("INNER RADIUS=" + dictEDdataOutput["INNER RADIUS"] + os.linesep)
    strFileOut.write("OUTER RADIUS=" + dictEDdataOutput["OUTER RADIUS"] + os.linesep)
    strFileOut.write("SCAN TYPE=" + dictEDdataOutput["SCAN TYPE"] + os.linesep)
    strFileOut.write("1 DEGREE AZ=" + dictEDdataOutput["1 DEGREE AZ"] + os.linesep)
    strFileOut.write("AZIMUTH BINS=" + dictEDdataOutput["AZIMUTH BINS"] + os.linesep)
    strFileOut.write("RADIAL BINS=" + dictEDdataOutput["RADIAL BINS"] + os.linesep)
    strFileOut.write("CONSERVE INT.=" + dictEDdataOutput["CONSERVE INT."] + os.linesep)
    strFileOut.write("POLARISATION=" + dictEDdataOutput["POLARISATION"] + os.linesep)
    strFileOut.write("GEOMETRY COR.=" + dictEDdataOutput["GEOMETRY COR."] + os.linesep)

# Experiment geometry parameters
    strFileOut.write("X-PIXEL SIZE=" + dictEDdataOutput["X-PIXEL SIZE"] + os.linesep)
    strFileOut.write("Y-PIXEL SIZE=" + dictEDdataOutput["Y-PIXEL SIZE"] + os.linesep)
    strFileOut.write("DISTANCE=" + dictEDdataOutput["DISTANCE"] + os.linesep)
    strFileOut.write("WAVELENGTH=" + dictEDdataOutput["WAVELENGTH"] + os.linesep)
    strFileOut.write("X-BEAM CENTRE=" + dictEDdataOutput["X-BEAM CENTRE"] + os.linesep)
    strFileOut.write("Y-BEAM CENTRE=" + dictEDdataOutput["Y-BEAM CENTRE"] + os.linesep)
    strFileOut.write("TILT ROTATION=" + dictEDdataOutput["TILT ROTATION"] + os.linesep)
    strFileOut.write("ANGLE OF TILT=" + dictEDdataOutput["ANGLE OF TILT"] + os.linesep)

# Mask and dimensions
    strFileOut.write("USE MASK=" + dictEDdataOutput["USE MASK"] + os.linesep)
    strFileOut.write("MASK FILE=" + dictEDdataOutput["MASK FILE"] + os.linesep)
    strFileOut.write("DIM1_DATA=" + dictEDdataOutput["DIM1_DATA"] + os.linesep)
    strFileOut.write("DIM2_DATA=" + dictEDdataOutput["DIM2_DATA"] + os.linesep)

# I/O parameters
    strFileOut.write("input_extn=" + dictEDdataOutput["input_extn"] + os.linesep)
    strFileOut.write("saving_format=" + dictEDdataOutput["saving_format"] + os.linesep)
    strFileOut.write("output_extn=" + dictEDdataOutput["output_extn"] + os.linesep)
    strFileOut.write("output_dir=" + dictEDdataOutput["output_dir"] + os.linesep)


def populateXSDataInputSPDCake(dictID11):
    xsDataInputSPDCake = XSDataInputSPDCake()
    # Angle of tilt
    xsDataInputSPDCake.setAngleOfTilt(XSDataAngle(float(dictID11["ANGLE OF TILT"])))

    # Dark current
    if dictID11["DARK CURRENT"] == "YES":
        xsDataInputSPDCake.setDarkCurrentImageFile(XSDataFile(XSDataString(dictID11["DC FILE"])))
        #xsDataFile = XSDataFile()
        #xsDataFile.setPath(XSDataString(dictID11["DC FILE "]))
        #xsDataInputSPDCake.setDarkCurrentImageFile(xsDataFile)

    if dictID11["FLAT-FIELD"] == "YES":
        xsDataInputSPDCake.setFlatFieldImageFile(XSDataFile(XSDataString(dictID11["FF FILE"])))

    if dictID11["FF SCALE"] == "NO":
        xsDataInputSPDCake.setFlatFieldImageFile(XSDataFile(XSDataString(dictID11["FF MULTIPLIER"])))

    if dictID11["SPATIAL DIS."] == "YES":
        xsDataInputSPDCake.setSpatialDistortionFile(XSDataFile(XSDataString(dictID11["SD FILE"])))

    xsDataInputSPDCake.setStartAzimuth(XSDataAngle(float(dictID11["START AZIMUTH"])))
    xsDataInputSPDCake.setStopAzimuth(XSDataAngle(float(dictID11["END AZIMUTH"])))
    xsDataInputSPDCake.setInnerRadius(XSDataDouble(float(dictID11["INNER RADIUS"])))
    xsDataInputSPDCake.setOuterRadius(XSDataDouble(float(dictID11["OUTER RADIUS"])))

    xsDataInputSPDCake.setBufferSizeX(XSDataInteger(int(dictID11["X-PIXEL SIZE"])))
    xsDataInputSPDCake.setBufferSizeY(XSDataInteger(int(dictID11["Y-PIXEL SIZE"])))
    xsDataInputSPDCake.setSampleToDetectorDistance(XSDataLength(float(dictID11["DISTANCE"])))
    xsDataInputSPDCake.setWavelength(XSDataLength(float(dictID11["WAVELENGTH"])))

    xsDataInputSPDCake.setBeamCentreInPixelsX(XSDataDouble(float(dictID11["X-BEAM CENTRE"])))
    xsDataInputSPDCake.setBeamCentreInPixelsY(XSDataDouble(float(dictID11["Y-BEAM CENTRE"])))
    xsDataInputSPDCake.setTiltRotation(XSDataAngle(float(dictID11["TILT ROTATION"])))
    xsDataInputSPDCake.setOutputFileType(XSDataFile(XSDataString(dictID11["saving_format"])))
    xsDataInputSPDCake.setOutputFileType(XSDataFile(XSDataString(dictID11["output_dir"])))

 # TODO : some parameters remain not inserted in this file because not in the datamodel   

    print xsDataInputSPDCake.marshal()






# some test

#dictionnaryData=readDataFile()
#EDWriteDataFile(dictionnaire)
#xsDataInputSPDCake = populateXSDataInputSPDCake(dictionnaryData)

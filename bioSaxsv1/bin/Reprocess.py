#!/usr/bin/env python
# -*- coding: utf8 -*-
#
#    Project: BioSaxs
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
__author__ = "Jérôme Kieffer"
__contact__ = "Jerome.Kieffer@ESRF.eu"
__license__ = "GPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"

import os, sys, time

# Append the EDNA kernel source directory to the python path
if not os.environ.has_key("EDNA_HOME"):
    pyStrProgramPath = os.path.abspath(sys.argv[0])
    pyLPath = pyStrProgramPath.split(os.sep)
    if len(pyLPath) > 3:
        pyStrEdnaHomePath = os.sep.join(pyLPath[:-3])
    else:
        print ("Problem in the EDNA_HOME path ..." + pyStrEdnaHomePath)
        sys.exit()
    os.environ["EDNA_HOME"] = pyStrEdnaHomePath

sys.path.append(os.path.join(os.environ["EDNA_HOME"], "kernel", "src"))
from EDFactoryPluginStatic  import EDFactoryPluginStatic
from EDVerbose              import EDVerbose
from EDLogging              import EDLogging
from EDParallelExecute      import EDParallelExecute
EDFactoryPluginStatic.loadModule("XSDataBioSaxsv1_0")
from XSDataBioSaxsv1_0      import XSDataInputBioSaxsProcessOneFilev1_0, \
    XSDataFile, XSDataString, XSDataInteger, XSDataDouble, XSDataImage, \
    XSDataBioSaxsSample, XSDataBioSaxsExperimentSetup
from XSDataCommon import XSDataLength, XSDataWavelength, XSDataFile, XSDataString, XSDataInteger, XSDataDouble, XSDataImage


EDNAPluginName = "EDPluginBioSaxsProcessOneFilev1_0"
LEN_INPUT_STR = 45

class BioSaxsReprocess(EDLogging):

    def __init__(self, code=None, comment=None, \
                 maskFile=None, normalization=None, imageSize=None, detector="pilatus", detectorDistance=None, pixelSize_1=None, pixelSize_2=None, beamCenter_1=None, beamCenter_2=None, wavelength=None,):
        EDLogging.__init__(self)
        self.comment = comment
        self.code = code
        self.maskFile = maskFile
        self.normalization = normalization

        self.detector = detector
        self.detectorDistance = detectorDistance
        if (detector == "pilatus") and (pixelSize_1 is None) and (pixelSize_2 is None):
            self.pixelSize_1 = 1.72e-4
            self.pixelSize_2 = 1.72e-4
        else:
            self.pixelSize_1 = pixelSize_1
            self.pixelSize_2 = pixelSize_2
        if (detector == "pilatus") and (beamCenter_1 is None) :
            self.imageSize = 4000000
        else:
            self.imageSize = imageSize
        self.beamCenter_1 = beamCenter_1
        self.beamCenter_2 = beamCenter_2
        self.wavelength = wavelength

        self.timeStamp = time.strftime("-%Y%m%d%H%M%S", time.localtime())
        self.dest1D = "1d" + self.timeStamp
        self.dest2D = "2d" + self.timeStamp
        self.destMisc = "misc" + self.timeStamp
        self.sample = XSDataBioSaxsSample()
        if code is not None:
            self.sample.code = XSDataString(code)
        if comment is not None:
            self.sample.comment = XSDataString(comment)
        self.experimentSetup = XSDataBioSaxsExperimentSetup()
        if self.detector:
            self.experimentSetup.detector = XSDataString(self.detector)
        if self.detectorDistance:
            self.experimentSetup.detectorDistance = XSDataLength(self.detectorDistance)
        if self.pixelSize_1:
            self.experimentSetup.pixelSize_1 = XSDataLength(self.pixelSize_1)
        if self.pixelSize_2:
            self.experimentSetup.pixelSize_2 = XSDataLength(self.pixelSize_2)
        if self.beamCenter_1:
            self.experimentSetup.beamCenter_1 = XSDataDouble(self.beamCenter_1)
        if self.beamCenter_2:
            self.experimentSetup.beamCenter_2 = XSDataDouble(self.beamCenter_2)
        if self.wavelength:
            self.experimentSetup.wavelength = XSDataWavelength(self.wavelength)

    def __repr__(self):
        lst = [
        "Sample comment:      %s" % self.comment, #
        "Sample code:         %s" % self.code, #
        "Mask file:           %s" % self.maskFile, #
        "Normalization factor: %s" % self.normalization ,
        "Raw image size:      %s" % self.imageSize, #
        "Detector type:       %s" % self.detector , #
        "Detector distance:   %s" % self.detectorDistance , #
        "Pixel size 1:        %s" % self.pixelSize_1,
        "Pixel size 2:        %s" % self.pixelSize_2 ,
        "Beam center 1:       %s" % self.beamCenter_1 ,
        "Beam center 2:       %s" % self.beamCenter_2 ,
        "Wavelength:          %s" % self.wavelength ]#
        return os.linesep.join(lst)

    def cliReadParam(self):
        print("Welcome to the Reprocessing of BioSaxs data. Enter '-' to re-use data from headers")

        raw = raw_input(("Sample code [%s]: " % self.code).ljust(LEN_INPUT_STR)).strip()
        if raw != "":
            self.code = raw

        raw = raw_input(("Sample comments [%s]: " % self.comment).ljust(LEN_INPUT_STR)).strip()
        if raw != "":
            self.comment = raw

        ok = False
        while not ok:
            raw = raw_input(("Wavelength (in meter) [%s]: " % self.wavelength).ljust(LEN_INPUT_STR)).strip()
            if raw == "-":
                 ok = True
            elif raw != "":
                try:
                    self.wavelenth = float(raw)
                    ok = True
                except Exception:
                    self.ERROR("Unable to convert to float: %s" % raw)
                    ok = False


        raw = raw_input(("Detector used [%s]:" % self.detector).ljust(LEN_INPUT_STR)).strip()
        if raw != "":
            self.detector = raw.lower()


        ok = False
        while not ok:
            raw = raw_input(("Detector image size in bytes [%s]: " % self.imageSize).ljust(LEN_INPUT_STR)).strip()
            if raw != "":
                try:
                    self.imageSize = float(raw)
                    ok = True
                except Exception:
                    self.ERROR("Unable to convert to float: %s" % raw)
                    ok = False
            else:
                ok = bool(self.imageSize)

        ok = False
        while not ok:
            raw = raw_input(("Mask file  [%s]: " % self.maskFile).ljust(LEN_INPUT_STR)).strip()
            if raw == "-":
                ok = True
            elif raw != "":
                self.maskFile = raw
                ok = True

            if  raw != "-" and ((self.maskFile is None) or (os.path.isfile(self.maskFile) is False)):
                ok = False

        ok = False
        while not ok:
            raw = raw_input(("Sample - Detector distance in meter [%s]: " % self.detectorDistance).ljust(LEN_INPUT_STR)).strip()
            if raw == "-":
                ok = True
            elif raw != "":
                try:
                    self.detectorDistance = float(raw)
                    ok = True
                except Exception:
                    self.ERROR("Unable to convert to float: %s" % raw)
                    ok = False


        ok = False
        while not ok:
            raw = raw_input(("Normalization factor [%s]: " % self.normalization).ljust(LEN_INPUT_STR)).strip()
            if raw == "-":
                ok = True
            elif raw != "":
                try:
                    self.normalization = float(raw)
                    ok = True
                except Exception:
                    self.ERROR("Unable to convert to float: %s" % raw)
                    ok = False

        ok = False
        while not ok:
            raw = raw_input(("Pixel size [%s %s]: " % (self.pixelSize_1, self.pixelSize_2)).ljust(LEN_INPUT_STR)).strip()
            if raw == "-":
                ok = True
            elif raw != "":
                lpx = raw.split()
                if len(lpx) == 1:
                    try:
                        self.pixelSize_1 = float(lpx[0])
                        self.pixelSize_2 = float(lpx[0])
                        ok = True
                    except Exception:
                        self.ERROR("Unable to convert to float: %s" % raw)
                        ok = False
                else:
                    try:
                        self.pixelSize_1 = float(lpx[0])
                        self.pixelSize_2 = float(lpx[1])
                        ok = True
                    except Exception:
                        self.ERROR("Unable to convert to float: %s" % raw)
                        ok = False
            else:
                if isinstance(self.pixelSize_1, (float, int)) and isinstance(self.pixelSize_2, (float, int)):
                     ok = True

        ok = False
        while not ok:
            raw = raw_input(("Beam Center position [%s %s]: " % (self.beamCenter_1, self.beamCenter_2)).ljust(LEN_INPUT_STR)).strip()
            if raw == "-":
                ok = True
            elif raw != "":
                lpx = raw.split()
                if len(lpx) == 1:
                    try:
                        self.beamCenter_1 = float(lpx[0])
                        self.beamCenter_2 = float(lpx[0])
                        ok = True
                    except Exception:
                        self.ERROR("Unable to convert to float: %s" % raw)
                        ok = False
                else:
                    try:
                        self.beamCenter_1 = float(lpx[0])
                        self.beamCenter_2 = float(lpx[1])
                        ok = True
                    except Exception:
                        self.ERROR("Unable to convert to float: %s" % raw)
                        ok = False
            else:
                if isinstance(self.beamCenter_1, (float, int)) and isinstance(self.beamCenter_2, (float, int)):
                     ok = True

        ###########################################
        if self.code is not None:
            self.sample.code = XSDataString(self.code)
        if self.comment is not None:
            self.sample.comment = XSDataString(self.comment)
        if self.detector is not None:
            self.experimentSetup.detector = XSDataString(self.detector)
        if self.detectorDistance is not None:
            self.experimentSetup.detectorDistance = XSDataLength(self.detectorDistance)
        if self.pixelSize_1 is not None:
            self.experimentSetup.pixelSize_1 = XSDataLength(self.pixelSize_1)
        if self.pixelSize_2 is not None:
            self.experimentSetup.pixelSize_2 = XSDataLength(self.pixelSize_2)
        if self.beamCenter_1 is not None:
            self.experimentSetup.beamCenter_1 = XSDataDouble(self.beamCenter_1)
        if self.beamCenter_2 is not None:
            self.experimentSetup.beamCenter_2 = XSDataDouble(self.beamCenter_2)
        if self.maskFile is not None:
            self.experimentSetup.maskFile = XSDataFile(XSDataString(self.maskFile))

    def toXml(self, filename):
        """Here we create the XML string to be passed to the EDNA plugin from the input filename
        This can / should be modified by the final user
        
        @param filename: full path of the input file
        @type filename: python string representing the path
        @rtype: XML string
        @return: python string  
        """

#        Is the file to process?
        dirname, basename = os.path.split(filename)
        rootDir, dirname = os.path.split(dirname)
        basename, ext = os.path.splitext(basename)
        if not ((dirname.lower() == "raw") and (ext.lower() == ".edf")):
            self.DEBUG("Not processing %s" % filename)
            return

        existing2DImage = os .path.join(rootDir, "2d", basename + ".edf")

        if os.path.isfile(existing2DImage):
#            print existing2DImage
            title = None
            for line in open(existing2DImage):
                if len(line) > 512:
                    break
                else:
                    line = line.strip()
                if line.startswith("title"):
                    title = line.split("=", 1)[-1]
                if line.startswith("Center_1")and (self.beamCenter_1 is None):
                    try:
                        self.experimentSetup.beamCenter_1 = XSDataDouble(float(line.split("=", 1)[-1].split()[0]))
                    except Exception:
                        self.ERROR("Reading from header: not a float " + line)
                elif line.startswith("Center_2")and (self.beamCenter_2 is None):
                    try:
                        self.experimentSetup.beamCenter_2 = XSDataDouble(float(line.split("=", 1)[-1].split()[0]))
                    except Exception:
                        self.ERROR("Reading from header: not a float " + line)
                elif line.startswith("PSize_1")and (self.pixelSize_1 is None):
                    try:
                        self.experimentSetup.pixelSize_1 = XSDataLength(float(line.split("=", 1)[-1].split()[0]))
                    except Exception:
                        self.ERROR("Reading from header: not a float " + line)
                elif line.startswith("PSize_2") and (self.pixelSize_2 is None):
                    try:
                        self.experimentSetup.pixelSize_2 = XSDataLength(float(line.split("=", 1)[-1].split()[0]))
                    except Exception:
                        self.ERROR("Reading from header: not a float " + line)
                elif line.startswith("SampleDistance") and (self.detectorDistance is None) :
                    try:
                        self.experimentSetup.detectorDistance = XSDataLength(float(line.split("=", 1)[-1].split()[0]))
                    except Exception:
                        self.ERROR("Reading from header: not a float " + line)
                elif line.startswith("WaveLength")and (self.wavelength is None):
                    try:
                        self.experimentSetup.wavelength = XSDataWavelength(float(line.split("=", 1)[-1].split()[0]))
                    except Exception:
                        self.ERROR("Reading from header: not a float " + line)
            if title:
                for block in title.split(","):
                    if "=" in block:
                        key, value = block.split("=", 1)
                    elif ":" in block:
                        key, value = block.split(":", 1)
                    else:
                        key = None
                    if key:
                        key = key.strip()
                        value = value.strip()
#                        print key, value
                        if key == "DiodeCurr":
                            try:
                                self.experimentSetup.beamStopDiode = XSDataDouble(float(value))
                            except Exception:
                                self.ERROR("Unable to convert %s to float" % block)
                        elif key == "MachCurr":
                            try:
                                self.experimentSetup.machineCurrent = XSDataDouble(float(value.split()[0]))
                            except Exception:
                                self.ERROR("Unable to convert %s to float" % block)
                        elif key == "Concentration":
                            try:
                                self.sample.concentration = XSDataDouble(float(value.split()[0]))
                            except Exception:
                                self.ERROR("Unable to convert %s to float" % block)
                        elif (key == "Comments") and (self.comment is None):
                                self.sample.comments = XSDataString(value.strip())
                        elif (key == "Code") and (self.code is None) :
                            self.sample.code = XSDataString(value.strip())
                        elif (key == "Mask") and (self.maskFile is None):
                            self.experimentSetup.maskFile = XSDataImage(XSDataString(value.strip()))
                        elif (key == "Normalisation") and (self.normalization is None):
                            try:
                                self.experimentSetup.normalizationFactor = XSDataDouble(float(value.split()[0]))
                            except Exception:
                                self.ERROR("Unable to convert %s to float" % block)


        xsd = XSDataInputBioSaxsProcessOneFilev1_0()
        xsd.rawImage = XSDataImage(XSDataString(filename))
        xsd.rawImageSize = XSDataInteger(self.imageSize)
        xsd.experimentSetup = self.experimentSetup
        xsd.sample = self.sample
        dir1d = os.path.join(rootDir, self.dest1D)
        dir2d = os.path.join(rootDir, self.dest2D)
        dirMisc = os.path.join(rootDir, self.destMisc)
        if not os.path.exists(dir1d):
            os.makedirs(dir1d)
        if not os.path.exists(dir2d):
            os.makedirs(dir2d)
        if not os.path.exists(dirMisc):
            os.makedirs(dirMisc)
        xsd.normalizedImage = XSDataImage(XSDataString(os.path.join(dir2d, basename + ".edf")))
        xsd.integratedImage = XSDataImage(XSDataString(os.path.join(dirMisc, basename + ".ang")))
        xsd.integratedCurve = XSDataFile(XSDataString(os.path.join(dir1d, basename + ".dat")))
#        print xsd.marshal()
        return xsd.marshal()

    def functError(self, xmlin):
        try:
            xsd = XSDataInputBioSaxsProcessOneFilev1_0.parseString(xmlin)
            filename = xsd.rawImage.path.value
        except Exception:
            filename = xmlin
        self.ERROR("Processing failed for: %s" % filename)


if __name__ == '__main__':
    paths = []
    mode = "OffLine"
    newerOnly = True
    debug = False
    for i in sys.argv[1:]:
        if i.lower().find("-online") in [0, 1]:
            mode = "dirwatch"
        elif i.lower().find("-all") in [0, 1]:
            newerOnly = False
        elif i.lower().find("-debug") in [0, 1]:
            debug = True
        if os.path.exists(i):
            paths.append(os.path.abspath(i))

    if len(paths) == 0:
        if mode == "OffLine":
            print "This is the Azimuthal Integration application of EDNA-BioSaxs, \nplease give a path to process offline or the option:\n\
            --online to process online incoming data in the given directory.\n\
            --all to process all existing files (unless they will be excluded)\n\
            --debug to turn on debugging mode in EDNA"

            sys.exit()
        else:
            paths = [os.getcwd()]

    cli = BioSaxsReprocess()
    print("#"*80 + os.linesep + "# Default configuration" + os.linesep + "#" * 80)
    print cli
    cli.cliReadParam()
    print("#"*80 + os.linesep + "# New configuration" + os.linesep + "#" * 80)
    print cli

    edna = EDParallelExecute(EDNAPluginName, _functXMLin=cli.toXml, _functXMLerr=cli.functError, _bVerbose=True, _bDebug=debug)
    edna.runEDNA(paths, mode , newerOnly)



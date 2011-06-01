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
__author__ = "Jérôme Kieffer"
__contact__ = "Jerome.Kieffer@ESRF.eu"
__license__ = "GPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"


import os, sys, shlex
from exceptions import IndexError, ValueError
# Append the EDNA kernel source directory to the python path
if not os.environ.has_key("EDNA_HOME"):
    pyStrProgramPath = os.path.abspath(sys.argv[0])
    pyLPath = pyStrProgramPath.split(os.sep)
    if len(pyLPath) > 5:
        pyStrEdnaHomePath = os.sep.join(pyLPath[:-3])
    else:
        print ("Problem in the EDNA_HOME path ..." + pyStrEdnaHomePath)
        sys.exit()
    os.environ["EDNA_HOME"] = pyStrEdnaHomePath
sys.path.append(os.path.join(os.environ["EDNA_HOME"], "kernel", "src"))

from EDVerbose import EDVerbose
from EDUtilsUnit import EDUtilsUnit
from EDFactoryPluginStatic import EDFactoryPluginStatic
from EDParallelExecute import EDParallelExecute
EDFactoryPluginStatic.loadModule("EDPluginSPDCakev1_5")
from EDPluginSPDCakev1_5 import EDPluginSPDCakev1_5
EDFactoryPluginStatic.loadModule("XSDataDiffractionCTv1")
from XSDataDiffractionCTv1 import XSDataInputDiffractionCT, XSDataDiffractionCTImage, XSDataDiffractionCTInstrument
from XSDataCommon import XSDataLength, XSDataString, XSDataInteger, XSDataAngle, \
    XSDataWavelength, XSDataFile, XSDataImage

EDNAPluginName = "EDPluginControlDiffractionCTv1_2"
class DiffractionCT(object):
    """
    class for the definition and the storage of the metadata as well as the XML generation. 
    """

    def __init__(self):
        """Constructor of the class"""
        self.pluginName = "EDPluginControlDiffractionCTv1_1"
        self.destinationDirectory = None
        self.sinogramFileNamePrefix = None
        self.powderDiffractionSubdirectory = None
        self.forceImage = None
        self.forceInstrument = None
        self.fastMotorSteps = None
        self.slowMotorSteps = None
        self.indexOffset = None
        self.powderDiffractionFormat = None
        self.listExtensions = []
        self.listExcludedPrefix = []
        self.listInput = []
        self.bNewerOnly = False
        self.strMode = "OffLine"

    def setup(self, _listInput=[], _mode="offline"):
        """Configure the various options"""

        bOK = False
        if _listInput == []:
            _listInput = [os.getcwd()]
        while not bOK:
            strtmp = raw_input("What are the input directories (mandatory, space separated) %s: " % _listInput).strip()
            if len(strtmp) > 0:
                bAllExists = True
                lstTemp = shlex.split(strtmp)
                for oneDir in shlex.split(strtmp):
                    if not os.path.exists(oneDir):
                        EDVerbose.screen("No such file or directory: %s" % oneDir)
                        bAllExists = False
                if bAllExists is True:
                    self.listInput = lstTemp
                    bOK = True
            else:
                self.listInput = _listInput
                bOK = True
        bOK = False
        while not bOK:
            strtmp = raw_input("What is operation mode [offline|online|all] (mandatory: %s): " % _mode).strip().lower()
            if len(strtmp) > 0:
                bOK = True
                if strtmp == "offline":
                    self.bNewerOnly = False
                    self.strMode = "OffLine"
                elif strtmp == "online":
                    self.bNewerOnly = True
                    self.strMode = "dirwatch"
                elif strtmp == "all":
                    self.bNewerOnly = False
                    self.strMode = "dirwatch"
                else:
                    bOK = False

        bOK = False
        while not bOK:
            strtmp = raw_input("What is the destination directory (mandatory): ").strip()
            if os.path.isdir(strtmp):
                self.destinationDirectory = XSDataFile()
                self.destinationDirectory.setPath(XSDataString(os.path.abspath(strtmp)))
                bOK = True

        bOK = False
        while not bOK:
            strtmp = raw_input("What is the sinogram filename prefix  (mandatory): ").strip()
            if strtmp != "":
                self.sinogramFileNamePrefix = XSDataString(strtmp)
                bOK = True

        bOK = False
        while not bOK:
            strtmp = raw_input("What is the powder diffraction subdirectory  (mandatory): ").strip()
            if strtmp != "":
                self.powderDiffractionSubdirectory = XSDataString(strtmp)
                bOK = True

        strtmp = raw_input("What is the powder diffraction output format (CHI or CIF, if any ): ").strip().lower()
        if strtmp.find("cif") >= 0:
            self.powderDiffractionFormat = XSDataString("cif")
        elif strtmp.find("chi") >= 0:
            self.powderDiffractionFormat = XSDataString("chi")

        strtmp = raw_input("Process all files ending with: ").strip()
        if len(strtmp) > 0:
            for oneExt in shlex.split(strtmp):
                self.listExtensions.append(oneExt)

        strtmp = raw_input("Exclude all files starting with: ").strip()
        if len(strtmp) > 0:
            for oneExt in shlex.split(strtmp):
                self.listExcludedPrefix.append(oneExt)

        strtmp = raw_input("Do you want to over-ride metadata from the headers [y|N]: ").strip().lower()
        if len(strtmp) > 0 and strtmp[0] == "y":

            strtmp = raw_input("What is the flat field image: ").strip()
            if os.path.isfile(strtmp):
                if self.forceImage is None:
                    self.forceImage = XSDataDiffractionCTImage()
                flatFieldImage = XSDataFile()
                flatFieldImage.setPath(XSDataString(os.path.abspath(strtmp)))
                self.forceImage.set_file_correction_image_flat_field(flatFieldImage)


            strtmp = raw_input("What is the dark current image: ").strip()
            if os.path.isfile(strtmp):
                if self.forceImage is None:
                    self.forceImage = XSDataDiffractionCTImage()
                darkCurrentImage = XSDataFile()
                darkCurrentImage.setPath(XSDataString(os.path.abspath(strtmp)))
                self.forceImage.set_file_correction_image_dark_current(darkCurrentImage)

            strtmp = raw_input("What is the mask file: ").strip()
            if os.path.isfile(strtmp):
                if self.forceImage is None:
                    self.forceImage = XSDataDiffractionCTImage()
                maskFile = XSDataFile()
                maskFile.setPath(XSDataString(strtmp))
                self.forceImage.set_file_correction_image_mask(maskFile)

            strtmp = raw_input("What is the spline file: ").strip()
            if os.path.isfile(strtmp):
                if self.forceImage is None:
                    self.forceImage = XSDataDiffractionCTImage()
                splineFile = XSDataFile()
                splineFile.setPath(XSDataString(os.path.abspath(strtmp)))
                self.forceImage.set_file_correction_spline_spatial_distortion(splineFile)

            strtmp = raw_input("What is the wavelength (like 0.7 A): ").replace("(", "").replace(")", "").strip()
            w = strtmp.split()
            if len(w) > 0:
                try:
                    f = float(w[0])
                except ValueError:
                    print("unable to understand what you said, skipping")
                else:
                    wavelength = XSDataWavelength()
                    wavelength.setValue(f)
                    if len(w) == 2:
                        wavelength.setUnit(XSDataString(w[1]))
                    if self.forceInstrument is None:
                        self.forceInstrument = XSDataDiffractionCTInstrument()
                    self.forceInstrument.set_diffrn_radiation_wavelength(wavelength)

            strtmp = raw_input("What is the distance between the sample and the detector along the beam: ").replace("(", "").replace(")", "").strip()
            w = strtmp.split()
            if len(w) > 0:
                try:
                    f = float(w[0])
                except ValueError:
                    print("unable to understand what you said, skipping")
                else:
                    distance = XSDataLength()
                    distance.setValue(f)
                    if len(w) == 2:
                        distance.setUnit(XSDataString(w[1]))
                    if self.forceInstrument is None:
                        self.forceInstrument = XSDataDiffractionCTInstrument()
                    self.forceInstrument.set_pd_instr_dist_spec_detc(distance)


            strtmp = raw_input("What is the pixel size (like 52.8 um 53.2 um): ").replace("(", "").replace(")", "").strip()
            w = strtmp.split()
            if len(w) > 0:
                xsdata1 = None
                xsdata2 = None
                if len(w) == 4:
                    try:
                        f1 = float(w[0])
                        f2 = float(w[2])
                    except ValueError:
                        print "Unable to convert to float !!! skipping"
                    else:
                        xsdata1 = XSDataLength()
                        xsdata1.setValue(f1)
                        xsdata1.setUnit(XSDataString(w[1]))
                        xsdata2 = XSDataLength()
                        xsdata2.setValue(f2)
                        xsdata2.setUnit(XSDataString(w[3]))
                elif len(w) == 2:
                    try:
                        f1 = float(w[0])
                        f2 = float(w[1])
                    except ValueError:
                        print "Unable to convert to float !!! skipping"
                    else:
                        xsdata1 = XSDataLength()
                        xsdata1.setValue(f1)
                        xsdata2 = XSDataLength()
                        xsdata2.setValue(f2)
                else:
                    print("unable to understand what you said, skipping")
                if (xsdata1 is not None) and (xsdata2 is not None):
                   if self.forceImage is None:
                        self.forceImage = XSDataDiffractionCTImage()
                   self.forceImage.set_array_element_size_1(xsdata1)
                   self.forceImage.set_array_element_size_2(xsdata2)

            strtmp = raw_input("What is the beam center in distance, not pixels (like 53.5 mm 48.2 mm): ").strip().replace("(", "").replace(")", "").strip()
            w = strtmp.split()
            if len(w) > 0:
                xsdata1 = None
                xsdata2 = None
                if len(w) == 4:
                    try:
                        f1 = float(w[0])
                        f2 = float(w[2])
                    except ValueError:
                        print "Unable to convert to float !!! skipping"
                    else:
                        xsdata1 = XSDataLength()
                        xsdata1.setValue(f1)
                        xsdata1.setUnit(XSDataString(w[1]))
                        xsdata2 = XSDataLength()
                        xsdata2.setValue(f2)
                        xsdata2.setUnit(XSDataString(w[3]))
                elif len(w) == 2:
                    try:
                        f1 = float(w[0])
                        f2 = float(w[1])
                    except ValueError, IndexError:
                        print "Unable to convert to float !!! skipping"
                    else:
                        xsdata1 = XSDataLength()
                        xsdata1.setValue(f1)
                        xsdata2 = XSDataLength()
                        xsdata2.setValue(f2)
                else:
                    print("unable to understand what you said, skipping")
                if (xsdata1 is not None) and (xsdata2 is not None):
                   if self.forceImage is None:
                        self.forceImage = XSDataDiffractionCTImage()
                   self.forceImage.set_diffrn_detector_element_center_1(xsdata1)
                   self.forceImage.set_diffrn_detector_element_center_2(xsdata2)

            strtmp = raw_input("What is the detector tilt angle: ").strip()
            tiltAngle = None
            try:
                tiltAngle = XSDataAngle(float(strtmp))
            except ValueError:
                print("unable to understand what you said, skipping")
            else:
                if self.forceImage is None:
                    self.forceImage = XSDataDiffractionCTImage()
                self.forceImage.set_pd_instr_special_details_tilt_angle(tiltAngle)

            strtmp = raw_input("What is the tilt plan rotation: ").strip()
            tiltRotation = None
            try:
                tiltRotation = XSDataAngle(float(strtmp))
            except ValueError:
                print("unable to understand what you said, skipping")
            else:
                if self.forceImage is None:
                    self.forceImage = XSDataDiffractionCTImage()
                self.forceImage.set_pd_instr_special_details_tilt_rotation(tiltRotation)


            strtmp = raw_input("What is the number of fast motor steps (you will have n+1 points): ").strip()
            try:
                self.fastMotorSteps = int(strtmp)
            except ValueError:
                fastMotorSteps = None
            else:
                if self.forceInstrument is None:
                    self.forceInstrument = XSDataDiffractionCTInstrument()
                self.forceInstrument.set_tomo_spec_displ_x_max(XSDataLength(self.fastMotorSteps))
                self.forceInstrument.set_tomo_spec_displ_x_min(XSDataLength(0))
                self.forceInstrument.set_tomo_spec_displ_x_inc(XSDataLength(1))
                self.forceInstrument.set_tomo_scan_type(XSDataString("flat"))

            strtmp = raw_input("What is the number of slow motor steps (you will have n+1 points): ").strip()
            try:
                self.slowMotorSteps = int(strtmp)
            except ValueError:
                self.slowMotorSteps = None
            else:
                if self.forceInstrument is None:
                    self.forceInstrument = XSDataDiffractionCTInstrument()
                self.forceInstrument.set_tomo_scan_ampl(XSDataLength(self.slowMotorSteps))
                self.forceInstrument.set_tomo_spec_displ_rotation_inc(XSDataLength(1))
                self.forceInstrument.set_tomo_scan_type(XSDataString("flat"))



            strtmp = raw_input("What is the index offset of your images: ").strip()
            try:
                self.indexOffset = int(strtmp)
            except ValueError:
                print("unable to understand what you said, skipping")



    def makeXML(self, filename):
        """Here we create the XML string to be passed to the EDNA plugin from the input filename
        This can / should be modified by the final user
        
        @param filename: full path of the input file
        @type filename: python string representing the path
        @rtype: XML string
        @return: python string  
        """
        bProcessFile = False
        basename = os.path.basename(filename)
        for oneExt in self.listExtensions:
            if basename.endswith(oneExt):
                bProcessFile = True
                break
        if bProcessFile:
            for onePref in self.listExcludedPrefix:
                if basename.startswith(onePref):
                    bProcessFile = False
        if not bProcessFile:
            EDVerbose.screen("Not processing file: %s" % filename)
            return
        xsdimage = XSDataImage()
        xsdimage.setPath(XSDataString(filename))
        xsd = XSDataInputDiffractionCT()
        xsd.setImage(xsdimage)
        xsd.setDestinationDirectory(self.destinationDirectory)
        xsd.setSinogramFileNamePrefix(self.sinogramFileNamePrefix)
        xsd.setPowderDiffractionSubdirectory(self.powderDiffractionSubdirectory)
        xsd.setPowderDiffractionFormat(self.powderDiffractionFormat)
        if self.indexOffset is not None and self.fastMotorSteps is not None:
            idx = 0
            basename = list(os.path.splitext(os.path.basename(filename))[0])
            basename.reverse()
            number = ""
            for i in basename:
                if i.isdigit():
                    number = i + number
                else: break
            idx = int(number) - self.indexOffset
            if idx < 0:return

            self.forceInstrument.set_tomo_spec_displ_x(XSDataLength(idx % (self.fastMotorSteps + 1)))
            self.forceInstrument.set_tomo_spec_displ_rotation(XSDataLength(idx // (self.fastMotorSteps + 1)))
        xsd.setOverrideScanParam(self.forceInstrument)
        xsd.setOverrideImageParam(self.forceImage)

        return xsd.marshal()


    def error(self, strXMLin):
        """
        This is an example of XMLerr function ... it prints only the name of the file created
        @param srXMLin: The XML string used to launch the job
        @type strXMLin: python string with the input XML
        @rtype: None
        @return: None     
        """
        xsd = XSDataInputDiffractionCT.parseString(strXMLin)
        filename = xsd.getImage().getPath().getValue
        EDVerbose.ERROR("Error in the processing of: %s" % filename)



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
            mode = "all"
            newerOnly = False
        elif i.lower().find("-debug") in [0, 1]:
            debug = True
        elif i.lower().find("-ncpu") in [0, 1]:
            iNbCPU = int(i.split("=", 1)[1])
        elif i.lower().find("-h") in [0, 1]:
            print "This is the DiffractionCTv1 application of EDNA %s, \nplease give a path to process offline or the option:\n\
            --online to process online incoming data in the given directory.\n\
            --all to process all existing files (unless they will be excluded)\n\
            --debug to turn on debugging mode in EDNA\n\
            --nCPU=xxx to specify the number of CPUs to use. Usually EDNA autodetects the number of processors." % EDNAPluginName
            sys.exit()
        elif os.path.exists(i):
            paths.append(os.path.abspath(i))


    dct = DiffractionCT()
    dct.setup(_listInput=paths, _mode=mode)

    edna = EDParallelExecute(EDNAPluginName, dct.makeXML, _functXMLerr=dct.error, _bVerbose=True, _bDebug=debug, _iNbThreads=iNbCPU)
    edna.runEDNA(dct.listInput, dct.strMode , dct.bNewerOnly)

    EDPluginSPDCakev1_5.killAllWorkers()


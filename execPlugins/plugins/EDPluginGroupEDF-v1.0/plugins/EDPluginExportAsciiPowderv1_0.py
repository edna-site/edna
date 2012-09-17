# coding: utf8
#
#    Project: PROJECT ExecPlugins EDF
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) ESRF
#
#    Principal author:       Jérôme Kieffer
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

__author__ = "Jerôme Kieffer"
__license__ = "GPLv3+"
__contact__ = "Jerome.Kieffer@esrf.eu"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"

import os, sys

from EDVerbose import EDVerbose
from EDPluginExec import EDPluginExec
from EDUtilsArray import EDUtilsArray
from XSDataEDFv1_0 import XSDataInput1DPowderEDF
from XSDataEDFv1_0 import XSDataResult1DPowderEDF
from XSDataCommon import XSDataFile, XSDataString
from EDUtilsUnit import EDUtilsUnit
from EDFactoryPluginStatic import EDFactoryPluginStatic
from EDUtilsPlatform   import EDUtilsPlatform

################################################################################
# AutoBuilder for Numpy, PIL and Fabio
################################################################################
architecture = EDUtilsPlatform.architecture
fabioPath = os.path.join(os.environ["EDNA_HOME"], "libraries", "FabIO-0.0.7", architecture)
imagingPath = os.path.join(os.environ["EDNA_HOME"], "libraries", "20091115-PIL-1.1.7", architecture)
numpyPath = os.path.join(os.environ["EDNA_HOME"], "libraries", "20090405-Numpy-1.3", architecture)
#scipyPath = os.path.join(os.environ["EDNA_HOME"], "libraries", "20090711-SciPy-0.7.1", architecture)
CifPath = os.path.join(os.environ["EDNA_HOME"], "libraries", "CifFile")

EDFactoryPluginStatic.preImport("numpy", numpyPath)
EDFactoryPluginStatic.preImport("fabio", fabioPath)
EDFactoryPluginStatic.preImport("Image", imagingPath)


try:
    import numpy
    from fabio.openimage import openimage
except Exception:
    EDVerbose.ERROR("Error in loading numpy,\n\
    Please re-run the test suite for EDTestSuitePluginExecThumbnailv10 \
    to ensure that all modules are compiled for you computer as they don't seem to be installed")


if  os.path.isdir(CifPath) and (CifPath not in sys.path):
    sys.path.insert(1, CifPath)
from CifFile import CIF

class EDPluginExportAsciiPowderv1_0(EDPluginExec):
    """
    Plugin to extract the data from an 1D powder diffraction pattern created with SPD.
    """

    def __init__(self):
        """
        Constructor of the class
        """
        EDPluginExec.__init__(self)
        self.setXSDataInputClass(XSDataInput1DPowderEDF)
        self.inputFilename = None
        self.outputFilename = None
        self.npaTwoTheta = None
        self.npaIntensities = None
        self.strFormat = "array" #default
        self.inputArray = None
        self.fPixelSize = None
        self.fAzimSize = None
        self.fDistance = None
        self.fRadOffset = 0
        self.fAzimOffset = 0
        self.fWavelength = None
        self.dHeader = {}
        self.iNbBins = None
        self.fDummy = 0
        self.fDeltaDummy = 0.01



    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        EDVerbose.DEBUG("EDPluginExportAsciiPowderv1_0.checkParameters")
        self.checkMandatoryParameters(self.getDataInput(), "Data Input is None")


    def preProcess(self, _edObject=None):
        """
        Preprocess: check the input parameters and unpack them
        """
        EDPluginExec.preProcess(self)
        EDVerbose.DEBUG("EDPluginExportAsciiPowderv1_0.preProcess")


        if self.getDataInput().getEdfFile() is not None:
            self.inputFilename = self.getDataInput().getEdfFile().getPath().getValue()
            if not os.path.isfile(self.inputFilename):
                EDVerbose.ERROR("The input file provided is not a valid file: %s" % self.inputFilename)
                raise RuntimeError("Not a valid file %s" % self.inputFilename)
            else:
                self.readArrayFromFile(self.inputFilename)

        elif self.getDataInput().getIntensities() is not None:
            self.inputArray = EDUtilsArray.xsDataToArray(self.getDataInput().getIntensities())

        else:
            strErrorMessage = "EDPluginExportAsciiPowderv1_0.preProcess: neither an input image, neither a data array given in input !"
            EDVerbose.ERROR(strErrorMessage)
            self.addErrorMessage(strErrorMessage)
            self.setFailure()
            raise ValueError, strErrorMessage

        if self.getDataInput().getDistance() is not None:
            self.fDistance = EDUtilsUnit.getSIValue(self.getDataInput().getDistance())

        if self.getDataInput().getPixelSize() is not None:
            self.fPixelSize = EDUtilsUnit.getSIValue(self.getDataInput().getPixelSize())

        if self.getDataInput().getOffset() is not None:
            self.fRadOffset = self.getDataInput().getOffset().getValue()

        if self.getDataInput().getOutputFormat() is not None:
            self.strFormat = self.getDataInput().getOutputFormat().getValue().lower()

        if self.getDataInput().getNumberOfBins() is not None:
            self.iNbBins = self.getDataInput().getNumberOfBins().getValue()

        if self.strFormat == "array":
            self.outputFilename = None
        else:
            if self.getDataInput().getOutputFile() is None:
                if "chi" in self.strFormat:
                    ext = ".chi"
                elif "cif" in self.strFormat:
                    ext = ".cif"
                elif "spr" in self.strFormat:
                    ext = ".spr"
                else:
                    ext = ".powder"
                self.outputFilename = os.path.join(self.getWorkingDirectory(), "output" + ext)
            else:
                self.outputFilename = self.getDataInput().getOutputFile().getPath().getValue()
                if os.path.isdir(self.outputFilename):
                    if "chi" in self.strFormat:
                        ext = ".chi"
                    elif "cif" in self.strFormat:
                        ext = ".cif"
                    elif "spr" in self.strFormat:
                        ext = ".spr"
                    else:
                        ext = ".powder"
                    self.outputFilename = os.path.join(self.outputFilename,
                                                       os.path.splitext(os.path.basename(self.inputFilename))[0] + ext)
        if (self.fPixelSize is None) or (self.fDistance is None):
            strErrorMessage = "EDPluginExportAsciiPowderv1_0.preProcess: pixel size: %s; distance: %s Cannot be identified in %s !!!!" % (self.fPixelSize, self.fDistance, self.inputFilename)
            EDVerbose.ERROR(strErrorMessage)
            self.addErrorMessage(strErrorMessage)
            self.setFailure()
            raise ValueError, strErrorMessage


    def process(self, _edObject=None):
        EDPluginExec.process(self)
        EDVerbose.DEBUG("EDPluginExportAsciiPowderv1_0.process")
        if len(self.inputArray.shape) == 2:
            iNbAzimBin, iLength = self.inputArray.shape
            if  iNbAzimBin == 1:
                nplInt = self.inputArray[0, :]
            else:
                nonNull = ((abs(self.inputArray - self.fDummy) > self.fDeltaDummy)).astype("int").sum(axis=0)
                nplInt = self.inputArray.sum(axis=0) / nonNull
        elif len(self.inputArray.shape) == 1:
            nplInt = self.inputArray
            iLength = len(nplInt)
        else:
            EDVerbose.ERROR("EDPluginExportAsciiPowderv1_0.inputArray has a large dimension: %s  " % (self.inputArray.shape))

        nplTth = numpy.degrees(numpy.arctan((numpy.arange(iLength) + 0.5 + self.fRadOffset) * self.fPixelSize / self.fDistance))

        if EDVerbose.isVerboseDebug():
            open("raw.dat", "wb").write("\n".join(["%s\t%s" % (nplTth[i], nplInt[i]) for i in range(len(nplInt))]))
            open("inputArray.xml", "wb").write(EDUtilsArray.arrayToXSData(nplInt, _bIncludeMd5sum=False).marshal())
        XRPD = lambda tth: numpy.interp(tth, nplTth, nplInt, left=0, right=0)

        tthMax = nplTth[-1]
        tthMin = nplTth[0]
        if (self.iNbBins is None):
            self.iNbBins = iLength
        pyfStep = (tthMax - tthMin) / (self.iNbBins - 1)

#        # Create the output data

        if "cif" in self.strFormat:
                cif = CIF()
                cif[ "_audit_creation_method"    ] = 'EDNA'
                cif[ "_pd_meas_2theta_range_inc" ] = str(pyfStep)
                cif[ "_pd_meas_2theta_range_max" ] = str(tthMax)
                cif[ "_pd_meas_2theta_range_min" ] = str(tthMin)
                cif[ "_pd_meas_number_of_points" ] = str(self.iNbBins)
                cif[ "_pd_meas_scan_method"      ] = "fixed"
                if "Title" in self.dHeader:
                    cif[ "_pd_spec_description"] = self.dHeader["Title"]
                if self.fWavelength is not None:
                    cif["_diffrn_radiation_wavelength"] = str(self.fWavelength * 1.0e10) #in Angstrom acording to CIF dict
                cif["_pd_instr_dist_spec/detc"] = str(self.fDistance * 1.0e3) #in mm acording to CIF dict
                oneloop = []
                for i in numpy.linspace(tthMin, tthMax, self.iNbBins):
                    oneloop.append({ "_pd_meas_intensity_total" : str(XRPD(i)) })
                cif["loop_"] = [ [ ["_pd_meas_intensity_total"], oneloop ] ]
                cif.saveCIF(self.outputFilename)

        elif "chi" in self.strFormat :
            f = open(self.outputFilename, "wb")
            if "Title" in self.dHeader:
                f.write(self.dHeader["Title"] + ": ")
            f.write("Angular Profile\nTwo-Theta Angle (degrees)\nIntensity (normalised)\n%i\n" % self.iNbBins)
            for i in numpy.linspace(tthMin, tthMax, self.iNbBins):
                f.write("%f\t%f\n" % (i, XRPD(i)))
            f.close()

        elif "spr" in self.strFormat :
            self.npaTwoTheta = numpy.linspace(tthMin, tthMax, self.iNbBins)
            f = open(self.outputFilename, "wb")
            f.write("# Generated by EDNA, Spread sheet with fortran order for fit2d compatibility" + os.linesep)
            f.write("# dim0 (radial values in degrees): " + "\t".join(["%.2f" % i for i in self.npaTwoTheta]) + os.linesep)
            f.write("# dim1 (azimuthal values in degrees): " + "\t".join(["%.2f" % i for i in numpy.degrees(self.fAzimSize * (numpy.arange(iNbAzimBin) + self.fAzimOffset))]) + os.linesep)
            f.write("%i,%i\tStartPixel=(1,1)" % (self.iNbBins, iNbAzimBin) + os.linesep)
            for i in xrange(iNbAzimBin):
                XRPD = lambda tth: numpy.interp(tth, nplTth, self.inputArray[i, :], left=0, right=0)
                f.write("\t".join(["%8.4f" % i for i in XRPD(self.npaTwoTheta)]) + os.linesep)
            f.close()
        else:
                self.npaTwoTheta = numpy.linspace(tthMin, tthMax, self.iNbBins)
                self.npaIntensities = XRPD(self.npaTwoTheta)


    def postProcess(self, _edObject=None):
        EDPluginExec.postProcess(self)
        EDVerbose.DEBUG("EDPluginExportAsciiPowderv1_0.postProcess")
        # Create some output data
        xsDataResult = XSDataResult1DPowderEDF()
        if self.outputFilename is None:
            xsDataResult.setTwoTheta(EDUtilsArray.arrayToXSData(self.npaTwoTheta))
            xsDataResult.setIntensity(EDUtilsArray.arrayToXSData(self.npaIntensities))
        else:
            xsdFile = XSDataFile()
            xsdFile.setPath(XSDataString(self.outputFilename))
            xsDataResult.setOutputFile(xsdFile)
        self.setDataOutput(xsDataResult)
        self.npaTwoTheta = None
        self.npaIntensities = None
        self.inputArray = None

    def readArrayFromFile(self, _filename):
        """
        Populate self.inputArray for a given filename and extracts as well 
        self.fPixelSize
        self.fDistance
        self.fRadOffset
        self.wavelength ...
        """

        image = openimage(_filename)
        self.inputArray = image.data
        self.dHeader = image.header
        if "Offset_1" in self.dHeader:
            offset, unit = self.dHeader["Offset_1"].split(None, 1)
            if unit.lower() != "pixel":
                EDVerbose.WARNING("I got a strange unit for offset: %s, I expected pixel." % self.dHeader["Offset_1"])
            try:
                self.fRadOffset = float(offset)
            except ValueError:
                strErrorMessage = "EDPluginExportAsciiPowderv1_0.process: Unable to recognize this offset and convert it to float: %s" % self.dHeader["Offset_1"]
                EDVerbose.ERROR(strErrorMessage)
                self.addErrorMessage(strErrorMessage)
                self.setFailure()
                raise ValueError, strErrorMessage

        if "Offset_2" in self.dHeader:
            offset, unit = self.dHeader["Offset_2"].split(None, 1)
            if unit.lower() != "pixel":
                EDVerbose.WARNING("I got a strange unit for offset: %s, I expected pixel." % self.dHeader["Offset_2"])
            try:
                self.fAzimOffset = float(offset)
            except ValueError:
                strErrorMessage = "EDPluginExportAsciiPowderv1_0.process: Unable to recognize this offset and convert it to float: %s" % self.dHeader["Offset_2"]
                EDVerbose.ERROR(strErrorMessage)
                self.addErrorMessage(strErrorMessage)
                self.setFailure()
                raise ValueError, strErrorMessage

        if "PSize_1" in self.dHeader:
            psize, unit = self.dHeader["PSize_1"].split(None, 1)
            try:
                fPixelSize = float(psize)
            except ValueError:
                strErrorMessage = "EDPluginExportAsciiPowderv1_0.process: Unable to recognize the radial pixel size and convert it to float: %s" % self.dHeader["PSize_1"]
                EDVerbose.ERROR(strErrorMessage)
                self.addErrorMessage(strErrorMessage)
                self.setFailure()
            else:
                self.fPixelSize = EDUtilsUnit.getValueLength(fPixelSize, unit)

        if "PSize_2" in self.dHeader:
            psize, unit = self.dHeader["PSize_2"].split(None, 1)
            try:
                fPixelSize = float(psize)
            except ValueError:
                strErrorMessage = "EDPluginExportAsciiPowderv1_0.process: Unable to recognize the azimuthal pixel size and convert it to float: %s" % self.dHeader["PSize_2"]
                EDVerbose.ERROR(strErrorMessage)
                self.addErrorMessage(strErrorMessage)
                self.setFailure()
            else:
                self.fAzimSize = EDUtilsUnit.getValueAngle(fPixelSize, unit)


        if ("SampleDistance" in self.dHeader):
            distance, unit = self.dHeader["SampleDistance"].split(None, 1)
            try:
                fDistance = float(distance)
            except ValueError:
                strErrorMessage = "EDPluginExportAsciiPowderv1_0.process: Unable to recognize the Sample Distance is and convert it to float: %s" % self.dHeader["SampleDistance"]
                EDVerbose.ERROR(strErrorMessage)
                self.addErrorMessage(strErrorMessage)
                self.setFailure()
                raise ValueError, strErrorMessage
            self.fDistance = EDUtilsUnit.getValueLength(fDistance, unit)

        if ("WaveLength" in self.dHeader):
            wavelenth, unit = self.dHeader["WaveLength"].split(None, 1)
            try:
                fWavelength = float(wavelenth)
            except ValueError:
                strErrorMessage = "EDPluginExportAsciiPowderv1_0.process: Unable to recognize the wavelength is and convert it to float: %s" % self.dHeader["WaveLength"]
                EDVerbose.ERROR(strErrorMessage)
                self.addErrorMessage(strErrorMessage)
                self.setFailure()
                raise ValueError, strErrorMessage
            self.fWavelength = EDUtilsUnit.getValueLength(fWavelength, unit)

        if ("Dummy" in self.dHeader):
            self.fDummy = float(self.dHeader.get("Dummy", 0))

        if ("DDummy" in self.dHeader):
            self.fDeltaDummy = float(self.dHeader.get("DDummy", 0.1))

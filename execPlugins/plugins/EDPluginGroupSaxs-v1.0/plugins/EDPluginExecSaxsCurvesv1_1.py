# coding: utf8
#
#    Project: ExecPlugins / Saxs Group / SaxsCurves
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2010 ESRF
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
from __future__ import with_statement

"""
Execution plugin for Saxs Curves:

Convert an image into an ascii file (spec like) radius

Nota: this is an execution plugin that "mimics the behavour of Saxs Curves" using Python-numpy

"""


__author__ = "Jérôme Kieffer"
__contact__ = "jerome.Kieffer@esrf.eu"
__license__ = "GPLv3+"
__copyright__ = "2011 - ESRF"
__date__ = "20110913"

import os
from EDVerbose              import EDVerbose
from EDPluginExec           import EDPluginExec
from XSDataCommon           import XSDataFile, XSDataString
from XSDataSaxsv1_0         import XSDataInputSaxsCurvesv1_0
from XSDataSaxsv1_0         import XSDataResultSaxsCurvesv1_0
from EDUtilsPlatform        import EDUtilsPlatform
from EDFactoryPluginStatic  import EDFactoryPluginStatic
architecture = EDUtilsPlatform.architecture
fabioPath = os.path.join(os.environ["EDNA_HOME"], "libraries", "FabIO-0.0.7", architecture)
imagingPath = os.path.join(os.environ["EDNA_HOME"], "libraries", "20091115-PIL-1.1.7", architecture)
numpyPath = os.path.join(os.environ["EDNA_HOME"], "libraries", "20090405-Numpy-1.3", architecture)

numpy = EDFactoryPluginStatic.preImport("numpy", numpyPath)
Image = EDFactoryPluginStatic.preImport("Image", imagingPath)
fabio = EDFactoryPluginStatic.preImport("fabio", fabioPath)

if fabio is None:
    strErr = """Error in loading numpy, PIL, fabio ,
    Please re-run the test suite for EDTestSuiteSaxs
    to ensure that all modules are compiled for you computer as they don't seem to be installed"""
    EDVerbose.ERROR(strErr)
    raise ImportError(strErr)



class EDPluginExecSaxsCurvesv1_1(EDPluginExec):
    """
    Numpy implementation of Saxs Curves
    """
    DO_NOT_PROPAGATE_EDF_KEYS = ["DATATYPE", "DIM_1", "DIM_2", "DUMMY", "DDUMMY",
                                 "OFFSET_1", "OFFSET_2", "CENTER_1", "CENTER_2", "BSIZE_1", "BSIZE_2", "PSIZE_1", "PSIZE_2",
                                 "COMPRESSION", "HEADERID", "IMAGE", "SIZE", "FILENAME", "AXISTYPE_1", "AXISTYPE_2",
                                 "EDF_DATABLOCKID", "EDF_BINARYSIZE", "EDF_HEADERSIZE", "BYTEORDER"]

    def __init__(self):
        """
        """
        EDPluginExec.__init__(self)
        self.setXSDataInputClass(XSDataInputSaxsCurvesv1_0)
        self.inputImage = None
        self.outputDataFile = None
        self.options = None
        self.headerMarker = "#"
        self.extraHeader = []

    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        self.DEBUG("EDPluginExecSaxsCurvesv1_1.checkParameters")
        self.checkMandatoryParameters(self.getDataInput(), "Data Input is None")


    def preProcess(self, _edObject=None):
        EDPluginExec.preProcess(self)
        self.DEBUG("EDPluginExecSaxsCurvesv1_1.preProcess")
        xsdIn = self.getDataInput()
        if  xsdIn.getInputImage() is not None:
            self.inputImage = xsdIn.getInputImage().getPath().getValue()
            if not os.path.isfile(self.inputImage):
                self.ERROR("Input file %s does not exist ... try to go on anyway" % self.inputImage)
        if xsdIn.getOutputDataFile() is not None:
            self.outputDataFile = xsdIn.getOutputDataFile().getPath().getValue()
        if xsdIn.getOptions() is not None:
            self.options = xsdIn.getOptions().getValue()
        for oneHeader in  xsdIn.getExtraHeaders():
            self.extraHeader.append(oneHeader.getValue())
        if xsdIn.getHeaderMarker() is not None:
            self.headerMarker = xsdIn.getHeaderMarker().getValue()

    def process(self, _edObject=None):
        """
        The numpy part
        """
        EDPluginExec.process(self)
        fabiofile = fabio.open(self.inputImage)
        npaSignal = fabiofile.data[0, :]
        npaStd = numpy.sqrt(fabiofile.next().data[0, :])
        fDistance = float(fabiofile.header["SampleDistance"])
        fPixelSize = float(fabiofile.header["PSize_1"])
        iOffset = int(fabiofile.header["Offset_1"])
        fWavelength = float(fabiofile.header["WaveLength"])
        fDummy = float(fabiofile.header["Dummy"])
        fDeltaDummy = float(fabiofile.header["DDummy"])
        npaQ = 4e-9 * numpy.pi / fWavelength * \
                    numpy.sin(numpy.arctan(numpy.linspace(start=(iOffset + 0.5) * fPixelSize / fDistance ,
                                         stop=(iOffset - 0.5 + fabiofile.dim1) * fPixelSize / fDistance ,
                                         num=fabiofile.dim1)) / 2)
        if "COMMENTS" in  fabiofile.capsHeader:
            keyComments = fabiofile.capsHeader["COMMENTS"]
        else:
            keyComments = None
#        if "CODE" in  fabiofile.capsHeader:
#            keyCode = fabiofile.capsHeader["CODE"]
#        else:
#            keyCode = None
        if "CONCENTRATION" in  fabiofile.capsHeader:
            keyConcentration = fabiofile.capsHeader["CONCENTRATION"]
        else:
            keyConcentration = None
        if "TITLE" in  fabiofile.capsHeader:
            keyTitle = fabiofile.capsHeader["TITLE"]
        else:
            keyTitle = None

        if keyComments:
            strComments = fabiofile.header[keyComments]
        elif keyTitle  and "Comments" in fabiofile.header[keyTitle]:
            strComments = fabiofile.header[keyTitle][fabiofile.header[keyTitle].find("Comments") + 9:].strip().split()[0][:-1]
        else:
            strComments = ""

#        if keyCode:
#            strCode = fabiofile.header[keyCode]
#        elif keyTitle and "Code" in fabiofile.header[keyTitle]:
#            strCode = fabiofile.header[keyTitle][fabiofile.header[keyTitle].find("Code") + 5:].strip().split()[0][:-1]
#        else:
#            strCode = ""

        if keyConcentration:
            strConcentration = fabiofile.header[keyConcentration]
        elif keyTitle and "Concentration" in fabiofile.header[keyTitle]:
            strConcentration = fabiofile.header[keyTitle][fabiofile.header[keyTitle].find("Concentration") + 14:].split()[0][:-1]
        else:
            strConcentration = ""

        lstStrOut = ["%s %s" % (self.headerMarker, strComments),
                     "%sSample c= %s mg/ml" % (self.headerMarker, strConcentration),
                     self.headerMarker]
        #Append the headers is needed
        for oneLine in self.extraHeader:
            lstStrOut.append(self.headerMarker + oneLine.strip())

        for key in fabiofile.header_keys:
            if key.upper() not in self.DO_NOT_PROPAGATE_EDF_KEYS:
                lstStrOut.append("%s %s = %s" % (self.headerMarker, key, fabiofile.header[key]))
        lstStrOut += [self.headerMarker,
                    "%s N 3" % self.headerMarker,
                    "%s L q*nm  I_%s  stddev" % (self.headerMarker, strComments),
#                    self.headerMarker,
#                    "%s Concentration: %s" % (self.headerMarker, strConcentration),
#                    "%s Code: %s" % (self.headerMarker, strCode)
                    ]
        for q, I, std in zip(npaQ, npaSignal, npaStd):
            if abs(I - fDummy) > fDeltaDummy:
                lstStrOut.append("%s  %s  %s" % (q, I, std))
        with open(self.outputDataFile, "wb") as f:
            f.write(os.linesep.join(lstStrOut))
            f.flush()


    def postProcess(self, _edObject=None):
        EDPluginExec.postProcess(self)
        self.DEBUG("EDPluginExecSaxsCurvesv1_1.postProcess")

        # Create some output data
        xsDataResult = XSDataResultSaxsCurvesv1_0()
        if self.outputDataFile is None:
            self.outputDataFile = "output.edf"
        if os.path.isfile(self.outputDataFile):
            xsdFile = XSDataFile()
            xsdFile.setPath(XSDataString(os.path.abspath(self.outputDataFile)))
            xsDataResult.setOutputDataFile(xsdFile)

        self.setDataOutput(xsDataResult)



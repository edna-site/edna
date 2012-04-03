# coding: utf8
#
#    Project: execPlugins
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2010, ESRF, Grenoble
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
from EDShare import EDShare
__author__ = "Jérôme Kieffer"
__contact__ = "Jerome.Kieffer@esrf.eu"
__license__ = "GPLv3+"
__copyright__ = "2010-2012, ESRF, Grenoble"
__status__ = "development"
__date__ = "20120313"

import os
from EDVerbose          import EDVerbose
from EDPluginExec       import EDPluginExec
from EDUtilsArray       import EDUtilsArray
from EDUtilsPlatform    import EDUtilsPlatform
from EDConfiguration    import EDConfiguration
from EDFactoryPlugin    import edFactoryPlugin as  EDFactoryPluginStatic
from EDUtilsPath        import EDUtilsPath
from EDThreading import Semaphore
from XSDataShiftv1_0    import XSDataInputShiftImage, XSDataResultShiftImage
from XSDataCommon       import XSDataImageExt, XSDataString
################################################################################
# AutoBuilder for Numpy, PIL and Fabio
################################################################################
architecture = EDUtilsPlatform.architecture
fabioPath = os.path.join(EDUtilsPath.EDNA_HOME, "libraries", "FabIO-0.0.7", architecture)
imagingPath = os.path.join(EDUtilsPath.EDNA_HOME, "libraries", "20091115-PIL-1.1.7", architecture)
numpyPath = os.path.join(EDUtilsPath.EDNA_HOME, "libraries", "20090405-Numpy-1.3", architecture)
scipyPath = os.path.join(EDUtilsPath.EDNA_HOME, "libraries", "20090711-SciPy-0.7.1", architecture)

numpy = EDFactoryPluginStatic.preImport("numpy", numpyPath)
scipy = EDFactoryPluginStatic.preImport("scipy", scipyPath)
EDFactoryPluginStatic.preImport("Image", imagingPath)
fabio = EDFactoryPluginStatic.preImport("fabio", fabioPath)


try:
    from fabio.edfimage import edfimage
    import  scipy.ndimage
except:
    EDVerbose.ERROR("Error in loading numpy, Scipy, PIL or Fabio,\n\
    Please re-run the test suite for EDTestSuitePluginExecShift \
    to ensure that all modules are compiled for you computer as they don't seem to be installed")


class EDPluginExecShiftImagev1_1(EDPluginExec):
    """
    Shift image by a given value.
    New in version 1.1: shift on a wider canvas (defined in configuration file)
         
    """
    FILL_KEY = "fill"
    MAX_OFFSET_KEY = "maxOffset"
    MAX_OFFSET_VALUE = 0
    FILL_VALUE = 0 #can be "min", "max", "mean"
    CONFIGURED = False
    _clsLock = Semaphore()

    def __init__(self):
        """
        Constructor of the plugin
        """
        EDPluginExec.__init__(self)
        self.setXSDataInputClass(XSDataInputShiftImage)
        self.npaImage = None
        self.tOffset = (0., 0.)
        self.strOutputImage = None
        self.strOutputType = None

    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        self.DEBUG("EDPluginExecShiftImagev1_0.checkParameters")
        self.checkMandatoryParameters(self.dataInput, "Data Input is None")
#No mandatory parameters

    def configure(self):
        """
        setup two configurations:
        --> MAX_OFFSET_VALUE 
        --> FILL_VALUE 
        
        """
        EDPluginExec.configure(self)
        if not self.__class__.CONFIGURED:
            with self.__class__._clsLock:
                if not self.__class__.CONFIGURED:
                    self.DEBUG("EDPluginExecShiftImagev1_1.configure")
                    xsPluginItem = self.getConfiguration()
                    if (xsPluginItem == None):
                        self.WARNING("EDPluginExecShiftImagev1_1.configure: No plugin item defined.")
                        xsPluginItem = XSPluginItem()
                    strFill = EDConfiguration.getStringParamValue(xsPluginItem, self.__class__.FILL_KEY)
                    if(strFill == None):
                        self.WARNING("EDPluginExecShiftImagev1_1.configure: No configuration parameter found for: %s using default value: %s\n%s"\
                                    % (self.FILL_KEY, self.FILL_VALUE, xsPluginItem.marshal()))
                    else:
                        strFill = strFill.strip().lower()
                        if strFill in ["min", "max", "mean"]:
                            self.__class__.FILL_VALUE = strFill
                        else:
                            try:
                                self.__class__.FILL_VALUE = float(strFill)
                            except ValueError, error:
                                self.ERROR("unable to convert %s to float: %s" % (strFill, error))
                    strMaxOffset = EDConfiguration.getStringParamValue(xsPluginItem, self.__class__.MAX_OFFSET_KEY)
                    if(strMaxOffset == None):
                        self.WARNING("EDPluginExecShiftImagev1_1.configure: No configuration parameter found for: %s using default value: %s\n%s"\
                                    % (self.MAX_OFFSET_KEY, self.MAX_OFFSET_VALUE, xsPluginItem.marshal()))
                    else:
                        if strMaxOffset.isdigit():
                            try:
                                self.__class__.MAX_OFFSET_VALUE = int(strMaxOffset)
                            except ValueError, error:
                                self.ERROR("unable to convert %s to int: %s" % (strMaxOffset, error))
                        else:
                            self.WARNING("EDPluginExecShiftImagev1_1.configure: No configuration parameter found for: %s using default value: %s\n%s"\
                                    % (self.MAX_OFFSET_KEY, self.MAX_OFFSET_VALUE, xsPluginItem.marshal()))
                    self.__class__.CONFIGURED = True

    def preProcess(self, _edObject=None):
        EDPluginExec.preProcess(self)
        self.DEBUG("EDPluginExecShiftImagev1_0.preProcess")
        sdi = self.dataInput
        if sdi.inputImage is not None:
            self.npaImage = numpy.array(EDUtilsArray.getArray(sdi.inputImage))
        elif  sdi.inputArray is not None:
            self.npaImage = EDUtilsArray.xsDataToArray(sdi.getInputArray())
        else:
            self.ERROR("EDPluginExecShiftImagev1_0.preProcess: You should either provide an images or an arrays, but I got: %s" % sdi.marshal())
            self.setFailure()
            raise RuntimeError

        offset = sdi.offset
        if len(offset) == 2:
            self.tOffset = (offset[0].value, offset[1].value)
        elif len(offset) == 1:
            self.tOffset = (offset[0].value, offset[0].value)

        if sdi.outputImage is not None:
            if sdi.outputImage.path is not None:
                self.strOutputType = "file"
                self.strOutputImage = sdi.outputImage.path.value
            if sdi.outputImage.shared is not None:
                self.strOutputType = "shared"
                self.strOutputImage = sdi.outputImage.shared.value
            if sdi.outputImage.array is not None:
                self.strOutputType = "array"



    def process(self, _edObject=None):
        EDPluginExec.process(self)
        self.DEBUG("EDPluginExecShiftImagev1_0.process")
        shapeIn = self.npaImage.shape
        shapeOut = tuple(2 * self.MAX_OFFSET_VALUE + i for i in shapeIn)
        if self.FILL_VALUE == "min":
            fFillValue = self.npaImage.min()
        elif self.FILL_VALUE == "max":
            fFillValue = self.npaImage.max()
        elif self.FILL_VALUE == "mean":
            fFillValue = self.npaImage.mean(dtype=float)
        elif isinstance(self.FILL_VALUE, float):
            fFillValue = self.FILL_VALUE
        else:
            fFillValue = 0.0
        npaOut = numpy.zeros(shapeOut, dtype="float32") + fFillValue
        npaOut[self.MAX_OFFSET_VALUE:self.MAX_OFFSET_VALUE + shapeIn[0],
               self.MAX_OFFSET_VALUE:self.MAX_OFFSET_VALUE + shapeIn[1]] = self.npaImage
        if self.tOffset != (0., 0.):
            self.npaImage = scipy.ndimage.shift(npaOut, self.tOffset, order=1, mode="constant", cval=fFillValue)
        else:
            self.npaImage = npaOut

    def postProcess(self, _edObject=None):
        EDPluginExec.postProcess(self)
        self.DEBUG("EDPluginExecShiftImagev1_0.postProcess")
        # Create some output data
        xsDataResult = XSDataResultShiftImage()
        if self.strOutputType is None:
            xsDataResult.setOutputArray(EDUtilsArray.arrayToXSData(self.npaImage))
        elif self.strOutputType == "file":
            image = edfimage(data=self.npaImage, header={"Offset_1":self.tOffset[0], "Offset_2":self.tOffset[1], "Max_Offset":self.MAX_OFFSET_VALUE})
            image.write(self.strOutputImage, force_type=self.npaImage.dtype)
            xsdimg = XSDataImageExt(path=XSDataString(self.strOutputImage))
            xsDataResult.outputImage = xsdimg
        elif self.strOutputType == "shared":
            EDShare[self.strOutputImage] = self.npaImage
            xsdimg = XSDataImageExt(shared=XSDataString(self.strOutputImage))
            xsDataResult.outputImage = xsdimg
        elif self.strOutputType == "array":
            xsdimg = XSDataImageExt(array=EDUtilsArray.arrayToXSData(self.npaImage))
            xsDataResult.outputImage = xsdimg

        self.setDataOutput(xsDataResult)
        self.npaImage = None


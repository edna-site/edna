# coding: utf8
#
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
__author__ = "Jérôme Kieffer"
__contact__ = "Jerome.Kieffer@esrf.eu"
__license__ = "GPLv3+"
__copyright__ = "2011, ESRF, Grenoble"
__date__ = "20110905"

import os, threading, time
from EDVerbose              import EDVerbose
from EDConfiguration        import EDConfiguration
from EDPluginExec           import EDPluginExec
from EDUtilsArray           import EDUtilsArray
from XSDataCommon           import XSPluginItem, XSDataDouble
from XSDataShiftv1_0        import XSDataInputMeasureOffset
from XSDataShiftv1_0        import XSDataResultMeasureOffset
from EDAssert               import EDAssert
from EDFactoryPluginStatic  import EDFactoryPluginStatic
from EDUtilsPlatform        import EDUtilsPlatform
from EDUtilsPath            import EDUtilsPath
from EDThreading            import Semaphore



################################################################################
# AutoBuilder for Numpy, PIL and Fabio
################################################################################
architecture = EDUtilsPlatform.architecture
fabioPath = os.path.join(EDUtilsPath.EDNA_HOME, "libraries", "FabIO-0.0.7", architecture)
imagingPath = os.path.join(EDUtilsPath.EDNA_HOME, "libraries", "20091115-PIL-1.1.7", architecture)
numpyPath = os.path.join(EDUtilsPath.EDNA_HOME, "libraries", "20090405-Numpy-1.3", architecture)
scipyPath = os.path.join(EDUtilsPath.EDNA_HOME, "libraries", "20090711-SciPy-0.7.1", architecture)
fftw3Path = os.path.join(EDUtilsPath.EDNA_HOME, "libraries", "pyfftw3-0.2.1", architecture)
numpy = EDFactoryPluginStatic.preImport("numpy", numpyPath)
EDFactoryPluginStatic.preImport("scipy.ndimage", scipyPath)
EDFactoryPluginStatic.preImport("scipy.fftpack", scipyPath)
EDFactoryPluginStatic.preImport("scipy.interpolate", scipyPath)
EDFactoryPluginStatic.preImport("scipy.signal", scipyPath)
Image = EDFactoryPluginStatic.preImport("Image", imagingPath)
fabio = EDFactoryPluginStatic.preImport("fabio", fabioPath)
fftw3 = EDFactoryPluginStatic.preImport("fftw3", fftw3Path)

try:
    import scipy.ndimage, scipy.interpolate
except:
    EDVerbose.ERROR("Error in loading numpy, Scipy, PIL or Fabio,\n\
    Please re-run the test suite for EDTestSuitePluginExecShift \
    to ensure that all modules are compiled for you computer as they don't seem to be installed")

srcDir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "src")
try:
    import imp
    MeasureOffset = imp.load_module(*(("MeasureOffset",) + imp.find_module("MeasureOffset", [srcDir])))
except ImportError, error:
    strErr = "Unable to load the MeasureOffset module from %s; %s" % (srcDir, error)
    EDVerbose.ERROR(strErr)
    raise ImportError(strErr)

class EDPluginExecMeasureOffsetv1_0(EDPluginExec):
    """
    An exec plugin that taked two images and measures the offset between the two.
    """
    __sem = Semaphore()
    __npaMask = None

    CONF_CONVOLUTION = None
    CONF_CONVOLUTION_KEY = "convolution"
    CONF_CONVOLUTION_DEFAULT = "numpy" #can be "numpy", "scipy, "fftpack" or "fftw". signal is no more possible

    def __init__(self):
        """
        """
        EDPluginExec.__init__(self)
        self.setXSDataInputClass(XSDataInputMeasureOffset)
        self.npaIm1 = None
        self.npaIm2 = None
        self.tOffset = None
        self.tCrop = None
        self.tCenter = None
        self.tWidth = None
        self.tSmooth = None
        self.bBackgroundsubtraction = False
        self.sobel = False




    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        self.DEBUG("EDPluginExecMeasureOffsetv1_0.checkParameters")
        self.checkMandatoryParameters(self.getDataInput(), "Data Input is None")

    def configure(self):
        """
        Configures the plugin from the configuration file with the following parameters
         - The CONVOLUTION method
        """
        EDPluginExec.configure(self)
        if self.CONF_CONVOLUTION is None:
            with self.__class__.__sem:
                self.DEBUG("EDPluginExecMeasureOffsetv1_0.configure")
                xsPluginItem = self.getConfiguration()
                if (xsPluginItem == None):
                    self.WARNING("EDPluginExecMeasureOffsetv1_0.configure: No plugin item defined.")
                    xsPluginItem = XSPluginItem()
                strCONVOLUTION = EDConfiguration.getStringParamValue(xsPluginItem, self.CONF_CONVOLUTION_KEY)
                if(strCONVOLUTION == None):
                    self.WARNING("EDPluginExecMeasureOffsetv1_0.configure: No configuration parameter found for: %s using default value: %s\n%s"\
                                % (self.CONF_CONVOLUTION_KEY, self.CONF_CONVOLUTION_DEFAULT, xsPluginItem.marshal()))
                    self.CONF_CONVOLUTION = self.CONF_CONVOLUTION_DEFAULT
                else:
                    self.CONF_CONVOLUTION = strCONVOLUTION.strip().lower()


    def preProcess(self, _edObject=None):
        EDPluginExec.preProcess(self)
        self.DEBUG("EDPluginExecMeasureOffsetv1_0.preProcess")
        sdi = self.getDataInput()
        images = sdi.getImage()
        arrays = sdi.getArray()

        if len(images) == 2:
            self.npaIm1 = numpy.array(EDUtilsArray.getArray(images[0]))
            self.npaIm2 = numpy.array(EDUtilsArray.getArray(images[1]))
        elif len(arrays) == 2:
            self.npaIm1 = EDUtilsArray.xsDataToArray(arrays[0])
            self.npaIm2 = EDUtilsArray.xsDataToArray(arrays[1])
        else:
            strError = "EDPluginExecMeasureOffsetv1_0.preProcess: You should either provide two images or two arrays, but I got: %s" % sdi.marshal()[:1000]
            self.ERROR(strError)
            self.setFailure()
            raise RuntimeError(strError)

        crop = sdi.getCropBorders()
        if len(crop) > 1 :
            self.tCrop = tuple([ i.getValue() for i in crop ])
        elif len(crop) == 1:
            self.tCrop = (crop[0].getValue(), crop[0].getValue())

        center = sdi.getCenter()
        if len(center) > 1:
            self.tCenter = tuple([ i.getValue() for i in center ])
        elif len(center) == 1:
            self.tCenter = (center[0].getValue(), center[0].getValue())

        width = sdi.getWidth()
        if len(width) > 1 :
            self.tWidth = tuple([i.getValue() for i in width])
        elif len(width) == 1:
            self.tWidth = (width[0].getValue(), width[0].getValue())

        smooth = sdi.getSmoothBorders()
        if len(smooth) == 2:
            self.tSmooth = (smooth[0].getValue(), smooth[1].getValue())
        elif len(smooth) == 1:
            self.tSmooth = (smooth[0].getValue(), smooth[0].getValue())

        if sdi.getBackgroundSubtraction() is not None:
            self.bBackgroundsubtraction = (sdi.getBackgroundSubtraction().getValue() in [1, True, "true"])

        if sdi.getSobelFilter() is not None:
            self.sobel = (sdi.getSobelFilter() in [1, True, "true"])
        EDAssert.equal(self.npaIm1.shape , self.npaIm2.shape, "Images have the same size")

    def process(self, _edObject=None):
        EDPluginExec.process(self)
        self.DEBUG("EDPluginExecMeasureOffsetv1_0.process")
        shape = self.npaIm1.shape
        if (self.tCrop is not None):
            d0min = min(shape[0], self.tCrop[0])
            d1min = min(shape[1], self.tCrop[1])
            d0max = max(0, shape[0] - self.tCrop[0])
            d1max = max(0, shape[1] - self.tCrop[1])
            shape = (d0max - d0min, d1max - d1min)
        else:
            d0min = 0
            d0max = shape[0]
            d1min = 0
            d1max = shape[1]

        if self.tCenter is None:
            #the default center is the geometry center of the image ... 
            self.tCenter = [ i // 2 for i in shape ]
        if self.tWidth is not None:
            d0min = max(0, self.tCenter[0] - (self.tWidth[0] // 2))
            d0max = min(shape[0], d0min + self.tWidth[0])
            d1min = max(0, self.tCenter[1] - (self.tWidth[1] // 2))
            d1max = min(shape[1], d1min + self.tWidth[1])
            shape = (d0max - d0min, d1max - d1min)
        if shape != self.npaIm1.shape:
            self.DEBUG("Redefining ROI to %s - %s ; %s - %s as crop=%s, center=%s and width=%s" % (d0min, d0max, d1min, d1max, self.tCrop, self.tCenter, self.tWidth))
            self.npaIm1 = self.npaIm1[d0min:d0max, d1min:d1max]
            self.npaIm2 = self.npaIm2[ d0min:d0max, d1min:d1max]
            shape = self.npaIm1.shape
            self.DEBUG("After Crop, images have shape : %s and %s " % (self.npaIm1.shape, self.npaIm2.shape))

        if self.bBackgroundsubtraction:
            self.DEBUG("performing background subtraction")
            x = range(shape[0] - 1) + [shape[0] - 1] * (shape[0] - 1) + range(shape[0] - 1, 0, -1) + [0] * (shape[0] - 1)
            y = [0] * (shape[1] - 1) + range(shape[1] - 1) + [shape[1] - 1] * (shape[1] - 1) + range(shape[1] - 1, 0, -1)
            spline1 = scipy.interpolate.SmoothBivariateSpline(x, y,
                    [self.npaIm1[x[i], y[i]] for i in xrange(len(x))], kx=1, ky=1)
            spline2 = scipy.interpolate.SmoothBivariateSpline(x, y,
                    [self.npaIm2[x[i], y[i]] for i in xrange(len(x))], kx=1, ky=1)
            self.npaIm1 -= spline1(range(shape[0]), range(shape[1]))
            self.npaIm2 -= spline2(range(shape[0]), range(shape[1]))

        if self.tSmooth is not None:
            self.npaIm1 *= EDPluginExecMeasureOffsetv1_0.getMask(shape, self.tSmooth)
            self.npaIm2 *= EDPluginExecMeasureOffsetv1_0.getMask(shape, self.tSmooth)

        if self.sobel:
            self.npaIm1 = scipy.ndimage.sobel(self.npaIm1)
            self.npaIm2 = scipy.ndimage.sobel(self.npaIm2)

        offset, logs = MeasureOffset.measure_offset(self.npaIm1, self.npaIm2,
                                                    self.CONF_CONVOLUTION, withLog=True)

        self.tOffset = [XSDataDouble(f) for f in offset]
        logs.insert(0, "")
        if len(logs) <= 4:
            self.DEBUG(os.linesep.join(logs))
        else:
            self.WARNING(os.linesep.join(logs))

    def postProcess(self, _edObject=None):
        EDPluginExec.postProcess(self)
        self.DEBUG("EDPluginExecMeasureOffsetv1_0.postProcess")
        # Create some output data
        xsDataResult = XSDataResultMeasureOffset()
        xsDataResult.setOffset(self.tOffset)
        self.setDataOutput(xsDataResult)



    @classmethod
    def getMask(cls, shape, sigma):
        """
        Generate a mask with 1 in the center and 0 on the border.
        
        @param shape: 2-tuple of integers: the shape of the final image
        @param sigma: 2-tuple of floats with the width of the border
        return: array 
        """
        with cls.__sem:
            if EDPluginExecMeasureOffsetv1_0.__npaMask == None:
                self.screen("got Shape=%s and Sigma=%s" % (shape, sigma))
                npa1 = numpy.ones(shape)
                npa2 = scipy.ndimage.interpolation.shift(npa1, (-2 * sigma[0], -2 * sigma[1]), mode='constant', cval=0.0 , order=0)
                npa3 = scipy.ndimage.interpolation.shift(npa2, sigma, mode='constant', cval=0.0 , order=0)
                npa4 = scipy.ndimage.gaussian_filter(npa3, sigma)
                EDPluginExecMeasureOffsetv1_0.__npaMask = npa4
                self.DEBUG("final matrix %s is %s" % (npa4.shape, npa4))
        return EDPluginExecMeasureOffsetv1_0.__npaMask

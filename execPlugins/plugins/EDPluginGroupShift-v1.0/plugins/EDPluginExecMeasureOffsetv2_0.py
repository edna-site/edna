# coding: utf8
#
#
#    Project: execPlugins
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2010-2012, ESRF, Grenoble
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
__copyright__ = "2012, ESRF, Grenoble"
__date__ = "20120914"

import os, threading, time, hashlib
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
################################################################################
# AutoBuilder for Numpy, PIL and Fabio
################################################################################
architecture = EDUtilsPlatform.architecture
fabioPath = os.path.join(EDUtilsPath.EDNA_HOME, "libraries", "FabIO-0.0.7", architecture)
imagingPath = os.path.join(EDUtilsPath.EDNA_HOME, "libraries", "20091115-PIL-1.1.7", architecture)
numpyPath = os.path.join(EDUtilsPath.EDNA_HOME, "libraries", "20090405-Numpy-1.3", architecture)
numpy = EDFactoryPluginStatic.preImport("numpy", numpyPath)
Image = EDFactoryPluginStatic.preImport("Image", imagingPath)
fabio = EDFactoryPluginStatic.preImport("fabio", fabioPath)
feature = EDFactoryPluginStatic.preImport("feature")
#
if feature is None:
    strErr = "Error in loading feature from https://github.com/kif/imageAlignment"
    EDVerbose.ERROR(strErr)
    raise ImportError(strErr)


class EDPluginExecMeasureOffsetv2_0(EDPluginExec):
    """
    An exec plugin that taked two images and measures the offset between the two using the SIFT algorithm. 
    """

    sift = feature.SiftAlignment()
    keyindex = {} #key = md5 of the image; value = idex of the keypoints of the image in the SIFT object

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
        self.DEBUG("EDPluginExecMeasureOffsetv2_0.checkParameters")
        self.checkMandatoryParameters(self.dataInput, "Data Input is None")


    def preProcess(self, _edObject=None):
        EDPluginExec.preProcess(self)
        self.DEBUG("EDPluginExecMeasureOffsetv2_0.preProcess")
        sdi = self.dataInput
        images = sdi.image
        arrays = sdi.array

        if len(images) == 2:
            self.npaIm1 = numpy.array(EDUtilsArray.getArray(images[0]))
            self.npaIm2 = numpy.array(EDUtilsArray.getArray(images[1]))
        elif len(arrays) == 2:
            self.npaIm1 = EDUtilsArray.xsDataToArray(arrays[0])
            self.npaIm2 = EDUtilsArray.xsDataToArray(arrays[1])
        else:
            strError = "EDPluginExecMeasureOffsetv2_0.preProcess: You should either provide two images or two arrays, but I got: %s" % sdi.marshal()[:1000]
            self.ERROR(strError)
            self.setFailure()
            raise RuntimeError(strError)

        crop = sdi.cropBorders
        if len(crop) > 1 :
            self.tCrop = tuple([ i.value for i in crop ])
        elif len(crop) == 1:
            self.tCrop = (crop[0].value, crop[0].value)

        center = sdi.center
        if len(center) > 1:
            self.tCenter = tuple([ i.value for i in center ])
        elif len(center) == 1:
            self.tCenter = (center[0].value, center[0].value)

        width = sdi.width
        if len(width) > 1 :
            self.tWidth = tuple([i.value for i in width])
        elif len(width) == 1:
            self.tWidth = (width[0].value, width[0].value)

        smooth = sdi.smoothBorders
        if len(smooth) == 2:
            self.tSmooth = (smooth[0].value, smooth[1].value)
        elif len(smooth) == 1:
            self.tSmooth = (smooth[0].value, smooth[0].value)

        if sdi.backgroundSubtraction is not None:
            self.bBackgroundsubtraction = (sdi.backgroundSubtraction.value in [1, True, "true"])

        if sdi.sobelFilter is not None:
            self.sobel = (sdi.sobelFilter in [1, True, "true"])
        EDAssert.equal(self.npaIm1.shape , self.npaIm2.shape, "Images have the same size")

    def process(self, _edObject=None):
        EDPluginExec.process(self)
        self.DEBUG("EDPluginExecMeasureOffsetv2_0.process")
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
            #array contiguity is needed for checksum calculation
            self.npaIm1 = numpy.ascontiguousarray(self.npaIm1[d0min:d0max, d1min:d1max])
            self.npaIm2 = numpy.ascontiguousarray(self.npaIm2[ d0min:d0max, d1min:d1max])
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
            self.npaIm1 *= MeasureOffset.make_mask(shape, self.tSmooth)
            self.npaIm2 *= MeasureOffset.make_mask(shape, self.tSmooth)

        if self.sobel:
            self.npaIm1 = scipy.ndimage.sobel(self.npaIm1)
            self.npaIm2 = scipy.ndimage.sobel(self.npaIm2)

        checksum1 = hashlib.md5(self.npaIm1).hexdigest()
        checksum2 = hashlib.md5(self.npaIm2).hexdigest()
        if checksum1 not in self.keyindex:
            self.keyindex[checksum1] = self.sift.sift(self.npaIm1)
        if checksum2 not in self.keyindex:
            self.keyindex[checksum2] = self.sift.sift(self.npaIm2)
        data = self.sift.match(self.keyindex[checksum1], self.keyindex[checksum2])
        v0 = data[:, 0] - data[:, 2]
        v1 = data[:, 1] - data[:, 3]
        self.tOffset = [XSDataDouble(numpy.median(v0)), XSDataDouble(numpy.median(v1))]


    def postProcess(self, _edObject=None):
        EDPluginExec.postProcess(self)
        self.DEBUG("EDPluginExecMeasureOffsetv2_0.postProcess")
        # Create some output data
        self.setDataOutput(XSDataResultMeasureOffset(offset=self.tOffset))


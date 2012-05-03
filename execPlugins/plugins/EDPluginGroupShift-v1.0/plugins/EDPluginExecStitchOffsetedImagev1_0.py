# coding: utf8
#
#    Project: execPlugins/shift
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2011, ESRF, Grenoble
#
#    Principal author:       Jerome Kieffer
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
__contact__ = "jerome.kieffer@esrf.fr"
__license__ = "GPLv3+"
__copyright__ = "2011, ESRF, Grenoble"

import os, time
from EDPluginExec           import EDPluginExec
from EDUtilsPlatform        import EDUtilsPlatform
from EDUtilsArray           import EDUtilsArray
from EDFactoryPluginStatic  import EDFactoryPluginStatic
from EDVerbose              import EDVerbose
from XSDataShiftv1_0        import XSDataInputStitchOffsetedImage, \
    XSDataResultStitchOffsetedImage, XSDataString, XSDataImageExt

################################################################################
# AutoBuilder for Numpy, PIL and Fabio
################################################################################
architecture = EDUtilsPlatform.architecture
fabioPath = os.path.join(os.environ["EDNA_HOME"], "libraries", "FabIO-0.0.7", architecture)
imagingPath = os.path.join(os.environ["EDNA_HOME"], "libraries", "20091115-PIL-1.1.7", architecture)
numpyPath = os.path.join(os.environ["EDNA_HOME"], "libraries", "20090405-Numpy-1.3", architecture)
scipyPath = os.path.join(os.environ["EDNA_HOME"], "libraries", "20090711-SciPy-0.7.1", architecture)

Image = EDFactoryPluginStatic.preImport("Image", imagingPath)
numpy = EDFactoryPluginStatic.preImport("numpy", numpyPath)
scipy = EDFactoryPluginStatic.preImport("scipy", scipyPath)
fabio = EDFactoryPluginStatic.preImport("fabio", fabioPath)

try:
    from fabio.edfimage import edfimage
    import scipy.ndimage
except Exception:
    EDVerbose.ERROR("Error in loading numpy, Scipy, PIL or Fabio,\n\
    Please re-run the test suite for EDTestSuitePluginExecShift \
    to ensure that all modules are compiled for you computer as they don't seem to be installed")


class EDPluginExecStitchOffsetedImagev1_0(EDPluginExec):
    """
    plugin that shifts a set of images and merge them togeather.
    """


    def __init__(self):
        """
        """
        EDPluginExec.__init__(self)
        self.setXSDataInputClass(XSDataInputStitchOffsetedImage)
        self._lImages = [] #list of ndarrays
        self._fDummy = 0
        self._lDummies = [] #list of 2-tuples of floats containing the dummy value and the delta-dummy
        self._lOffsets = [] #list of 2-tuples of floats containing the offset values
        self._strOutFile = None
        self._strBlending = "max" #can be min or mean or naive
        self._bAutoscale = False
        self._ndaResult = None
        self.tCenter = None
        self.tWidth = None
        self._strMask = None

    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        self.DEBUG("EDPluginExecStitchOffsetedImagev1_0.checkParameters")
        self.checkMandatoryParameters(self.getDataInput(), "Data Input is None")
        self.checkMandatoryParameters(self.getDataInput().getInputImages(), "No Input OffetedImages")

    def preProcess(self, _edObject=None):
        EDPluginExec.preProcess(self)
        self.DEBUG("EDPluginExecStitchOffsetedImagev1_0.preProcess")
        sdi = self.getDataInput()
        for ofImage in sdi.getInputImages():
            if (ofImage.file is not None) and os.path.isfile(ofImage.file.path.value):
                self._lImages.append(EDUtilsArray.getArray(ofImage.file))
            elif (ofImage.array is not None):
                self._lImages.append(EDUtilsArray.xsDataToArray(ofImage.array))
            else:
                strError = "EDPluginExecStitchOffsetedImagev1_0.preProcess: You need to provide either an image file either an array; I got: %s !!!" % ofImage.marshal()
                self.ERROR(strError)
                raise RuntimeError(strError)
            dummy = [0.0, 0.001]
            if ofImage.dummyValue is not None:
                dummy[0] = ofImage.dummyValue.value
            if ofImage.deltaDummy is not None:
                dummy[1] = ofImage.deltaDummy.value
            self._lDummies.append(tuple(dummy))
            if ofImage.offset not in [list(), None]:
                offset = [i.value for i in ofImage.offset ]
            else:
                offset = [0, 0]
            self._lOffsets.append(tuple(offset))
        if sdi.blending is not None:
            self._strBlending = sdi.blending.value
        if sdi.dummyValue is not None:
            self._fDummy = sdi.dummyValue.value
        if sdi.outputImage is not None:
            self._strOutFile = sdi.outputImage.path.value
        if sdi.autoscale is not None:
            self._bAutoscale = bool(sdi.autoscale.value)
        if sdi.mask is not None:
            self._strMask = sdi.mask.path.value
            if not os.path.isfile(self._strMask):
                self._strMask = None

        center = sdi.centerROI
        if len(center) > 1:
            self.tCenter = tuple([ i.value for i in center ])
        elif len(center) == 1:
            self.tCenter = (center[0].value, center[0].value)

        width = sdi.widthROI
        if len(width) > 1 :
            self.tWidth = tuple([i.value for i in width])
        elif len(width) == 1:
            self.tWidth = (width[0].value, width[0].value)


    def process(self, _edObject=None):
        EDPluginExec.process(self)
        self.DEBUG("EDPluginExecStitchOffsetedImagev1_0.process")


        shiftedImage = []
        distanceSq = lambda t2f: (t2f[0] * t2f[0] + t2f[1] * t2f[1])
        ref = self._lOffsets[0]
        refOffset = distanceSq(ref)
        shape = self._lImages[0].shape
        if self._strMask:
            mask = (1 - fabio.open(self._strMask).data).astype("bool")
        else:
            mask = 0
        for img, offset, dummy in zip(self._lImages, self._lOffsets, self._lDummies):
            shImg = scipy.ndimage.shift(img, offset, cval=dummy[0], order=0)
            if dummy[1] == 0:
                if self._strMask:
                    shImgMasked = numpy.ma.MaskedArray(shImg,
                                    (shImg == dummy[0]) + scipy.ndimage.shift(mask, offset, cval=1, order=0))
                else:
                    shImgMasked = numpy.ma.MaskedArray(shImg, (shImg == dummy[0]))
            else:
                if self._strMask:
                    shImgMasked = numpy.ma.MaskedArray(shImg,
                                    (abs(shImg - dummy[0]) <= dummy[1]) + scipy.ndimage.shift(mask, offset, cval=1, order=0))
                else:
                    shImgMasked = numpy.ma.MaskedArray(shImg, (abs(shImg - dummy[0]) <= dummy[1]))
            shiftedImage.append(shImgMasked)
            if (offset != ref) and (distanceSq(offset) < refOffset):
                ref = offset
                refOffset = distanceSq(offset)
        refIdx = self._lOffsets.index(ref)

        if EDVerbose.isVerboseDebug():
            e = edfimage(data=shiftedImage[0].filled(self._fDummy),
                         header={"Dummy":str(self._fDummy), "Offset_1":str(self._lOffsets[0][0]), "Offset_2":str(self._lOffsets[0][1])})
            for img, offset in zip(shiftedImage[1:], self._lOffsets[1:]):
                e.appendFrame(data=img.filled(self._fDummy),
                              header={"Dummy":str(self._fDummy), "Offset_1":str(offset[0]), "Offset_2":str(offset[1])})
            e.write("stack.edf")


        ROI = False
        if self.tCenter is None:
            #the default center is the geometry center of the image ... 
            self.tCenter = [ i // 2 for i in shape ]
        if self.tWidth is not None:
            d0min = max(0, self.tCenter[0] - (self.tWidth[0] // 2))
            d0max = min(shape[0], d0min + self.tWidth[0])
            d1min = max(0, self.tCenter[1] - (self.tWidth[1] // 2))
            d1max = min(shape[1], d1min + self.tWidth[1])
            shape = (d0max - d0min, d1max - d1min)
        else:
            d0min = 0
            d0max = shape[0]
            d1min = 0
            d1max = shape[1]
        refImg = shiftedImage[refIdx]
        stackMaskedImg = numpy.ma.zeros((len(self._lOffsets), refImg.shape[0], refImg.shape[1]))
        self.screen("ROI[%s:%s, %s:%s]\t Autoscale: %s\tBlending method: %s" % (d0min, d0max, d1min, d1max, self._bAutoscale, self._strBlending))
        if self._bAutoscale:
            for idx, img in enumerate(shiftedImage):
                ratio = (refImg[d0min:d0max, d1min:d1max] / img[d0min:d0max, d1min:d1max])
                stackMaskedImg[idx] = ratio.mean() * img
        else:
            for idx, img in enumerate(shiftedImage):
                stackMaskedImg[idx] = img



        if self._strBlending.lower().startswith("naive"):
            npaTempBool = numpy.cumsum((1 - stackMaskedImg.mask), axis=0) * (1 - stackMaskedImg.mask) == 1
            result = numpy.ma.MaskedArray((npaTempBool * stackMaskedImg.data).sum(axis=0), stackMaskedImg.mask.prod(axis=0))

        elif self._strBlending.lower().startswith("max"):
            result = stackMaskedImg.max(axis=0)
        elif self._strBlending.lower().startswith("min"):
            result = stackMaskedImg.min(axis=0)
        else: #self._strBlending.lower() == "mean":
            result = stackMaskedImg.mean(axis=0)

        self._ndaResult = result.filled(self._fDummy)

    def postProcess(self, _edObject=None):
        EDPluginExec.postProcess(self)
        self.DEBUG("EDPluginExecStitchOffsetedImagev1_0.postProcess")
        # Create some output data
        xsDataResult = XSDataResultStitchOffsetedImage()
        if self._strOutFile is not None:
            edf = edfimage(data=self._ndaResult, header={"Dummy":str(self._fDummy), "Blending":self._strBlending, "Autoscale":str(self._bAutoscale)})
            edf.write(self._strOutFile)
            xsDataResult.setOutputImage(XSDataImageExt(path=XSDataString(self._strOutFile)))
        else:
            xsDataResult.setOutputArray(EDUtilsArray.arrayToXSData(self._ndaResult))
        self.setDataOutput(xsDataResult)


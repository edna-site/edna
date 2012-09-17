# coding: utf8
#
#    Project: execPlugins: Thumbnail generator
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) European Synchrotron Radiation Facility, Grenoble, France
#
#    Principal author:       Jérôme Kieffer (Jerome.Kieffer@esrf.eu)
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
__contact__ = "Jerome.Kieffer@esrf.eu"
__license__ = "GPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"


import os, threading, tempfile #sys
from EDVerbose              import EDVerbose
from EDPluginExec           import EDPluginExec
from EDUtilsArray           import EDUtilsArray
from EDFactoryPluginStatic  import EDFactoryPluginStatic
from XSDataCommon           import XSDataFile
from XSDataCommon           import XSDataString
from XSDataExecThumbnail    import XSDataInputExecThumbnail
from XSDataExecThumbnail    import XSDataResultExecThumbnail
from EDUtilsPlatform        import EDUtilsPlatform

################################################################################
# AutoBuilder for Numpy, PIL and Fabio
################################################################################
architecture = EDUtilsPlatform.architecture
fabioPath = os.path.join(os.environ["EDNA_HOME"], "libraries", "FabIO-0.0.7", architecture)
imagingPath = os.path.join(os.environ["EDNA_HOME"], "libraries", "20091115-PIL-1.1.7", architecture)
numpyPath = os.path.join(os.environ["EDNA_HOME"], "libraries", "20090405-Numpy-1.3", architecture)
scipyPath = os.path.join(os.environ["EDNA_HOME"], "libraries", "20090711-SciPy-0.7.1", architecture)

EDFactoryPluginStatic.preImport("numpy", numpyPath)
EDFactoryPluginStatic.preImport("fabio", fabioPath)
EDFactoryPluginStatic.preImport("Image", imagingPath)
EDFactoryPluginStatic.preImport("scipy", scipyPath)
EDFactoryPluginStatic.preImport("scipy.ndimage.morphology", scipyPath)

try:
    import numpy, Image, fabio, scipy, scipy.ndimage.morphology
except Exception:
    EDVerbose.ERROR("Error in loading numpy, PIL, fabio or scipy,\n\
    Please re-run the test suite for EDTestSuitePluginExecThumbnailv10 \
    to ensure that all modules are compiled for you computer as they don't seem to be installed")
    raise

import ImageFile, ImageOps
ImageFile.MAXBLOCK = 1000000 # default is 64k
#import fabio.openimage
from fabio.openimage import openimage







class EDPluginExecThumbnailv10(EDPluginExec):
    """
    This is the excution plugin called Thumbnail that creates a JPEG (or PNG) thumbnail image from a CCD image 
    It makes use of both Fabio, PIL and Numpy libraries. So please check that those three libraries, all located 
    at  $EDNA_HOME/libraries have been compiled for your computer.
    """
    __palette = None
    __semaphore = threading.Semaphore()
    default_colormap = """
0 0 0
0 0 1
1 0 1
1 0 0
1 1 0
1 1 1
"""

    def __init__(self):
        """
        Constructor of the plugin 
        """
        EDPluginExec.__init__(self)
        self.setXSDataInputClass(XSDataInputExecThumbnail)
        self.inputFilename = None
        self.thumbFormat = None
        self.colorize = None
        self.keepRatio = None
        self.gamma = None
        self.invert = None
        self.equalize = None
        self.autocontrast = None
        self.output = None
        self.format = None
        self.height = None
        self.width = None
        self.normalize = None
        self.npaImage = None
        self.cropBorders = None
        self.log = None
        self.minLevel = None
        self.maxLevel = None
        self.minLevelUnit = None
        self.maxLevelUnit = None
        self.gaussianBlur = None
        self.dilatation = None


    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        EDVerbose.DEBUG("EDPluginExecThumbnailv10.checkParameters")
        self.checkMandatoryParameters(self.getDataInput(), "Data Input is None")
#        self.checkMandatoryParameters(self.getDataInput().getInputImagePath().getPath().getValue(), "No Input image")


    def preProcess(self, _edObject=None):
        """
        Preprocess of the plugin: 
        check parameters and extract from EDNA format into something more simple & pythonic
        """
        EDPluginExec.preProcess(self)
        EDVerbose.DEBUG("EDPluginExecThumbnailv10.preProcess")
        sdi = self.getDataInput()
        if sdi.getInputImagePath() is not None:
            self.inputFilename = sdi.getInputImagePath().getPath().getValue()
            if not os.path.isfile(self.inputFilename):
                EDVerbose.ERROR("The input file provided is not a valid file: " + self.inputFilename)
                raise "Not a valid file " + self.inputFilename
        elif sdi.getInputArray() is not None:
            self.npaImage = EDUtilsArray.xsDataToArray(sdi.getInputArray())
        else:
            strError = "You should either provide an input filename or an array, you provided: %s" % sdi.marshal()
            EDVerbose.ERROR(strError)
            self.setFailure()
            raise RuntimeError(strError)

        self.colorize = False
        if sdi.getLevelsColorize() is not None:
            if sdi.getLevelsColorize().getValue() in [1, "true", "True", True]:
                self.colorize = True
                EDVerbose.DEBUG("EDPluginExecThumbnailv10 Set colorize")


        self.equalize = False
        if sdi.getLevelsEqualize() is not None:
            if sdi.getLevelsEqualize().getValue() in [1, "true", "True", True]:
                self.equalize = True
                EDVerbose.DEBUG("EDPluginExecThumbnailv10 Set equalize")

        self.normalize = False
        if sdi.getLevelsNormalize() is not None:
            if sdi.getLevelsNormalize().getValue() in [1, "true", "True", True]:
                self.normalize = True
                EDVerbose.DEBUG("EDPluginExecThumbnailv10 Set normalize")

#        Shall we swap white and black ?
        self.invert = False
        if sdi.getLevelsInvert() is not None:
            if sdi.getLevelsInvert().getValue() in [1, "true", "True", True]:
                self.invert = True
                EDVerbose.DEBUG("EDPluginExecThumbnailv10 Set invert")

#        Should we apply a gamma correction to the image, something in the range 0.2 - 1.0 should be nice 
        self.gamma = 1
        if sdi.getLevelsGamma() is not None:
            self.gamma = sdi.getLevelsGamma().getValue()
            EDVerbose.DEBUG("EDPluginExecThumbnailv10 Set gamma")

#        Shall we keep the ration of the image 
        self.keepRatio = True
        if sdi.getKeepRatio() is not None:
            if not sdi.getKeepRatio().getValue() in [1, "true", "True", True]:
                self.keepRatio = False
                EDVerbose.DEBUG("EDPluginExecThumbnailv10 Set keepRatio to False")

#        self.height=512
        if sdi.getThumbHeight() is not None:
            self.height = sdi.getThumbHeight().getValue()
            EDVerbose.DEBUG("EDPluginExecThumbnailv10 Set height")
#        self.width=512
        if sdi.getThumbWidth() is not None:
            self.width = sdi.getThumbWidth().getValue()
            EDVerbose.DEBUG("EDPluginExecThumbnailv10 Set width")

#        Set the output format, by defaul JPEG
        self.format = "jpg"
        if sdi.getThumbFormat() is not None:
            self.format = sdi.getThumbFormat().getValue().lower()
            EDVerbose.DEBUG("EDPluginExecThumbnailv10 Set output format")

        self.log = False
        if sdi.getLevelsLog() is not None:
            if sdi.getLevelsLog().getValue() in [1, "true", "True", True]:
                self.log = True
                EDVerbose.DEBUG("EDPluginExecThumbnailv10 Set log")

        if sdi.getLevelsAutoContrast() is not None:
            self.autocontrast = float(sdi.getLevelsAutoContrast().getValue())
            EDVerbose.DEBUG("EDPluginExecThumbnailv10 Set autocontrast with cut-off at %s%%" % self.autocontrast)


        self.cropBorders = [i.getValue() for i in sdi.getCropBorders()]
        EDVerbose.DEBUG("EDPluginExecThumbnailv10 crop borders by %s" % self.cropBorders)

        if sdi.getLevelsMin() is not None:
            self.minLevel = sdi.getLevelsMin().getValue()
            if sdi.getLevelsMin().getUnit() is not None:
                self.minLevelUnit = sdi.minLevel.getUnit().getValue()
            EDVerbose.DEBUG("EDPluginExecThumbnailv10 Set minimum level to %s %s" % (self.minLevel, self.minLevelUnit))

        if sdi.getLevelsMax() is not None:
            self.maxLevel = sdi.getLevelsMax().getValue()
            if sdi.getLevelsMax().getUnit() is not None:
                self.maxLevelUnit = sdi.getLevelsMax().getUnit().getValue()
            EDVerbose.DEBUG("EDPluginExecThumbnailv10 Set Maximum level to %s %s" % (self.maxLevel, self.maxLevelUnit))

        self.gaussianBlur = [i.getValue() for i in sdi.getFilterBlur()]
        EDVerbose.DEBUG("EDPluginExecThumbnailv10 gaussian blur with kernel size:  %s" % self.gaussianBlur)

        self.dilatation = [i.getValue() for i in sdi.getFilterDilatation()]
        EDVerbose.DEBUG("EDPluginExecThumbnailv10 Dilatation filter  %s" % self.dilatation)


#       keep this at the end of preprocess
        if sdi.getOutputPath() is None:
            if self.inputFilename is  None:
                id, self.output = tempfile.mkstemp(prefix="output", dir=self.getWorkingDirectory(), suffix="." + self.format)
            else:
                if not os.path.isfile(os.path.splitext(self.inputFilename)[0] + "." + self.format):
                    self.output = os.path.splitext(self.inputFilename)[0] + "." + self.format
                else:
                    self.output = os.path.join(self.getWorkingDirectory(), os.path.splitext(os.path.basename(self.inputFilename)) [0] + "." + self.format)
        else:
            path = sdi.getOutputPath().getPath().getValue()
            dirname = os.path.dirname(path)
            if not os.path.isdir(dirname):
                os.makedirs(dirname, int("777", 8))
            if path.endswith(os.sep) and not os.path.isdir(path):
                os.makedirs(dirname, int("777", 8))
            if os.path.isdir(path):
                if self.inputFilename is  None:
                    id, self.output = tempfile.mkstemp(prefix="output", dir=path, suffix="." + self.format)
                else:
                    self.output = os.path.join(path, os.path.splitext(os.path.basename(self.inputFilename)) [0] + "." + self.format)
            else:
                self.output = path


    def process(self, _edObject=None):
        """
        This is the main method of the plugin, it does the job, not the EDNA name conversions which were done in the preprocess. 
        """

        EDPluginExec.process(self)
        EDVerbose.DEBUG("EDPluginExecThumbnailv10.process")

#        try:
#        except Exception:
#        edfImage = EDF(self.inputFilename)
#        self.npaImage = edfImage.GetData(0)

#        Read the image using FABIO
        isRGB = False
        pilOutputImage = None
        if self.inputFilename is not None:
            try:
                fabioImage = openimage(self.inputFilename)
                self.npaImage = fabioImage.data
            except Exception:
                pilInputImage = Image.open(self.inputFilename)
                x, y = pilInputImage.size
                ImageFile.MAXBLOCK = x * y
                if pilInputImage.mode == "1":
                    self.npaImage = numpy.asarray(pilInputImage).astype("uint8")
                    isRGB = False
                elif pilInputImage.mode == "F":
                    self.npaImage = numpy.asarray(pilInputImage)
                    isRGB = False
                elif pilInputImage.mode == "L":
                    self.npaImage = numpy.asarray(pilInputImage)
                    isRGB = False
                elif pilInputImage.mode == "P":
                    self.npaImage = numpy.asarray(pilInputImage.convert("RGB"))
                    isRGB = True
                elif pilInputImage.mode == "RGB":
                    self.npaImage = numpy.asarray(pilInputImage)
                    isRGB = True
                elif pilInputImage.mode == "CMJK":
                    self.npaImage = numpy.asarray(pilInputImage.convert("RGB"))
                    isRGB = True

        dtype = self.npaImage.dtype
        NPAImageFloat = None

# crop border
        if len(self.cropBorders) > 0:

            if len(self.cropBorders) == 1:
                crop0 = self.cropBorders[0]
                crop1 = self.cropBorders[0]
            else:
                crop0 = self.cropBorders[0]
                crop1 = self.cropBorders[1]
            if isRGB:
                self.npaImage = self.npaImage[crop0:-crop0, crop1:crop1, :]
            else:
                self.npaImage = self.npaImage[crop0:-crop0, crop1:crop1]


# Set maxima and minima
        if (self.minLevelUnit is not None) or (self.maxLevelUnit is not None):
            sortedArray = self.npaImage.flatten()
            sortedArray.sort()

        if self.minLevel is not None:
            self.normalize = True
            if isRGB:
                EDVerbose.warning("It is not allowed  to set Min with RGB data")
            else:
                if self.minLevelUnit in ["%", "percent"]:
                    self.minLevel = sortedArray[int(round(float(self.minLevel) * sortedArray.size / 100.0))]
                if isinstance(self.npaImage[0, 0], int):
                    self.npaImage = numpy.maximum(self.npaImage, int(self.minLevel) * numpy.ones_like(self.npaImage))
                else:
                    self.npaImage = numpy.maximum(self.npaImage, self.minLevel * numpy.ones_like(self.npaImage))

        if self.maxLevel is not None:
            self.normalize = True
            if isRGB:
                EDVerbose.warning("It is not allowed  to set Max with RGB data")
            else:
                if self.maxLevelUnit in ["%", "percent"]:
                    self.maxLevel = sortedArray[int(round(float(self.maxLevel) * sortedArray.size / 100.0))]
                if isinstance(self.npaImage[0, 0], int):
                    self.npaImage = numpy.minimum(self.npaImage, int(self.maxLevel) * numpy.ones_like(self.npaImage))
                else:
                    self.npaImage = numpy.minimum(self.npaImage, self.maxLevel * numpy.ones_like(self.npaImage))

# Scipy filters come here:
        if len(self.gaussianBlur) > 0:
            if len(self.gaussianBlur) == 1 :
                kernel = (self.gaussianBlur[0], self.gaussianBlur[0])
            else:
                kernel = (self.gaussianBlur[0], self.gaussianBlur[1])
            if isRGB:
                kernel = (kernel[0], kernel[1], 0)
            self.npaImage = scipy.ndimage.gaussian_filter(self.npaImage, kernel)

        if len(self.dilatation) > 0:
            if len(self.dilatation) == 1:
                kernel = (self.dilatation[0], self.dilatation[0])
            else:
                kernel = (self.dilatation[0], self.dilatation[1])
            if isRGB:
                kernel = (kernel[0], kernel[1], 0)
            self.npaImage = scipy.ndimage.morphology.grey_dilation(self.npaImage, kernel)


#Normalization ; equalization
        if (self.normalize is True) or (self.equalize is True):
            if isRGB is True:
                self.npaImage = numpy.asarray(ImageOps.equalize(Image.fromarray(self.npaImage)))
            else:
                EDVerbose.DEBUG("EDPluginExecThumbnailv10: Normalization")
                vmin = self.npaImage.min()
                vmax = self.npaImage.max()
                NPAImageFloat = (self.npaImage.astype(numpy.float32) - float(vmin)) / (float(vmax) - float(vmin))
                if (self.equalize == True):
                    nbr_bins = 64
                    NPAImageFloatFlat = NPAImageFloat.flatten()
                    imhist, bins = numpy.histogram(NPAImageFloatFlat, nbr_bins, normed=True)  #get image histogram
                    cdf = imhist.cumsum() #cumulative distribution function
                    ncdf = cdf / cdf[-1]  #normalized cumulative distribution function
#                    print ncdf
                    NPAImageFloat2Flat = numpy.interp(NPAImageFloatFlat, bins, [0] + ncdf.tolist())
                    NPAImageFloat = NPAImageFloat2Flat.reshape(NPAImageFloat.shape)
                    EDVerbose.DEBUG("Equalize: min= %f, max= %f" % (NPAImageFloat.min(), NPAImageFloat.max()))

#Gamma and logarithm scale
        if ((self.log is True) or (self.gamma != 1)) and (NPAImageFloat is None): # then we need the array in float  
            if dtype == numpy.uint8:
                NPAImageFloat = self.npaImage.astype(numpy.float32) / 255.0
            elif dtype == numpy.uint16:
                NPAImageFloat = self.npaImage.astype(numpy.float32) / 65535.0
            else:
                NPAImageFloat = self.npaImage.astype(numpy.float32)

        if self.log is True:
            NPAImageFloat = numpy.log(1 - NPAImageFloat.min() + NPAImageFloat)
            vmin = NPAImageFloat.min()
            vmax = NPAImageFloat.max()
            NPAImageFloat = (NPAImageFloat - vmin) / (vmax - vmin)

        if self.gamma != 1:
            if dtype not in [numpy.uint8, numpy.uint16]:
                vmin = NPAImageFloat.min()
                vmax = NPAImageFloat.max()
                NPAImageFloat = (NPAImageFloat - vmin) / (vmax - vmin)
            NPAImageInt = (255.0 * (NPAImageFloat ** self.gamma)).astype("uint8")

        else: #if (self.gamma == 1):
            if NPAImageFloat is None:
                if dtype == numpy.uint8:
                    NPAImageInt = self.npaImage
                elif dtype == numpy.uint16:
                    NPAImageInt = (self.npaImage / 256).astype(numpy.uint8)
                else: #for float or a signed integer
                    vmin = self.npaImage.min()
                    vmax = self.npaImage.max()
                    NPAImageInt = ((self.npaImage.astype(numpy.float32) - vmin) / (vmax - vmin) * 255.0).astype(numpy.uint8)
            else:
                vmin = NPAImageFloat.min()
                vmax = NPAImageFloat.max()
                EDVerbose.DEBUG("EDPluginExecThumbnailv10:   NPAImageFloat => NPAImageInt min=%s max =%s" % (vmin, vmax))
                NPAImageInt = ((NPAImageFloat - vmin) * 255.0 / (vmax - vmin)).astype(numpy.uint8)
#COnversion back to PIL mode
        if isRGB is True:
            pilOutputImage = Image.fromarray(NPAImageInt, 'RGB')
        else:
            pilOutputImage = Image.fromarray(NPAImageInt, 'L')

        if (self.autocontrast is not None):
            pilOutputImage = ImageOps.autocontrast(pilOutputImage, self.autocontrast)

        if (self.width is not None) or  (self.height is not None):
            if (self.width > 0) and (self.height > 0):
                if self.keepRatio is True:
#                    PIL takes care of the ratio
                    pilOutputImage.thumbnail((self.width, self.height), Image.ANTIALIAS)
                else:
                    pilOutputImage = pilOutputImage.resize((self.width, self.height), Image.ANTIALIAS)
            else:
                if self.width is None:
                    pilOutputImage.thumbnail((self.height, self.height), Image.ANTIALIAS)
                elif self.height is None:
                    pilOutputImage.thumbnail((self.width, self.width), Image.ANTIALIAS)

        if self.invert == True:
            pilOutputImage = ImageOps.invert(pilOutputImage)
        if self.colorize == True:
            pilOutputImage.putpalette(EDPluginExecThumbnailv10.getPalette())
            pilOutputImage = pilOutputImage.convert("RGB")

        self.synchronizeOn()
        if self.format == "jpg":
            self.width, self.height = pilOutputImage.size
            if self.width * self.height > ImageFile.MAXBLOCK:
                ImageFile.MAXBLOCK = self.width * self.height
            try:
                pilOutputImage.save(self.output, "JPEG", quality=85, optimize=True)
            except TypeError:
                pilOutputImage.save(self.output)
        else:
            pilOutputImage.save(self.output)
        self.synchronizeOff()

    def postProcess(self, _edObject=None):
        """
        Postprocess of the plugin:
         
        * set output of the plugin
        * free some memory from large arrays
        """
        EDPluginExec.postProcess(self)
        EDVerbose.DEBUG("EDPluginExecThumbnailv10.postProcess")
        # Create some output data

        xsDataResult = XSDataResultExecThumbnail()
        if os.path.isfile(self.output):
            xsDataFile = XSDataFile()
            xsDataFile.setPath(XSDataString(self.output))
            xsDataResult.setThumbnailPath(xsDataFile)
            xsDataString = XSDataString()
            xsDataString.setValue(self.format)
            xsDataResult.setThumbnailType(xsDataString)
        self.setDataOutput(xsDataResult)
        self.npaImage = None

    @staticmethod
    def getPalette(colormap=None):
        """ convert a matlab type colormap to a PIL palette 
        @param colormap: "R G B\nR G B\n ...
        @type colormap: string
        @return a palette
        """
        if EDPluginExecThumbnailv10.__palette is None:
            EDPluginExecThumbnailv10.__semaphore.acquire()
            if EDPluginExecThumbnailv10.__palette is None:
                if colormap is None:
                    colormap = EDPluginExecThumbnailv10.default_colormap
                npa = numpy.array([ 255 * float(i) for i in colormap.split()])
                size = npa.size / 3
                npb = npa.reshape((size, 3))
                steps = [ float(i) / (size - 1) for i in range(size)]
                r = lambda x:numpy.interp(x, steps, npb[:, 0])
                g = lambda x:numpy.interp(x, steps, npb[:, 1])
                b = lambda x:numpy.interp(x, steps, npb[:, 2])
                palette = [ (int(r(i / 255.)), int(g(i / 255.)), int(b(i / 255.))) for i in range(256)]
                palette = map(lambda a: chr(a[0]) + chr(a[1]) + chr(a[2]), palette)
                EDPluginExecThumbnailv10.__palette = "".join(palette)
            EDPluginExecThumbnailv10.__semaphore.release()
        return EDPluginExecThumbnailv10.__palette

#
# coding: utf8
#
#    Project: Image Filter
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2011, ESRF
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
from EDUtilsArray import EDUtilsArray

__author__ = "Jérôme Kieffer"
__license__ = "GPLv3+"
__copyright__ = "2011, ESRF"

import os, threading

from EDVerbose import EDVerbose
from EDPluginExec import EDPluginExec
from XSDataCommon import XSDataImage, XSDataString
from XSDataImageFilter import XSDataInputMedianFilter
from XSDataImageFilter import XSDataResultMedianFilter
from EDFactoryPluginStatic import EDFactoryPluginStatic
from EDUtilsPlatform   import EDUtilsPlatform


################################################################################
# AutoBuilder for Numpy, PIL and Fabio
################################################################################
architecture = EDUtilsPlatform.architecture
fabioPath = os.path.join(os.environ["EDNA_HOME"], "libraries", "FabIO-0.0.7", architecture)
imagingPath = os.path.join(os.environ["EDNA_HOME"], "libraries", "20091115-PIL-1.1.7", architecture)
numpyPath = os.path.join(os.environ["EDNA_HOME"], "libraries", "20090405-Numpy-1.3", architecture)
scipyPath = os.path.join(os.environ["EDNA_HOME"], "libraries", "20090711-SciPy-0.7.1", architecture)
EDFactoryPluginStatic.preImport("numpy", numpyPath)
EDFactoryPluginStatic.preImport("scipy", scipyPath)
EDFactoryPluginStatic.preImport("fabio", fabioPath)
EDFactoryPluginStatic.preImport("Image", imagingPath)

try:
    import fabio
    import scipy
    import numpy
except Exception:
    EDVerbose.ERROR("Error in loading numpy, Scipy, PIL or Fabio,\n\
    Please re-run the test suite for EDTestSuitePluginFilterImage \
    to ensure that all modules are compiled for you computer as they don't seem to be installed")

################################################################################################
###############  Class Ordered dictionary limited in size           ############################
################################################################################################

class ImageCache(dict):
    __sem = threading.Semaphore()
    def __init__(self, maxSize=100):
        dict.__init__(self)
        self.__ordered = []
        self.__maxSize = maxSize
#        self.size = 0

    def __setitem__(self, key, value):
        """x.__setitem__(i, y) <==> x[i]=y"""
        self.__sem.acquire()
        if key in self.__ordered:
            index = self.__ordered.index(key)
            self.__ordered.pop(index)
        if len(self) > self.__maxSize:
            firstKey = self.__ordered[ 0 ]
            EDVerbose.DEBUG("Removing file %s from cache" % firstKey)
            dict.pop(self, firstKey)
            self.__ordered = self.__ordered[1:]
        self.__ordered.append(key)
        self.__sem.release()
        dict.__setitem__(self, key, value)

    def __getitem__(self, key):
        """x.__getitem__(y) <==> x[y]"""
        self.__sem.acquire()
        index = self.__ordered.index(key)
        self.__ordered.append(key)
        self.__ordered.pop(index)
        data = dict.__getitem__(self, key)
        self.__sem.release()
        return data

    def keys(self):
        """ returns the list of keys, ordered"""
        #self.__sem.acquire()
        data = self.__ordered[:]
        #self.__sem.release()
        return data

    def pop(self, key):
        """remove a key for the dictionary and return it's value"""
        self.__sem.acquire()
        try:
            index = self.__ordered.index(key)
        except Exception:
            raise KeyError
        self.__ordered.pop(index)
        myData = self.imageDict.pop(key)
        self.__sem.release()
        return myData

    def getMaxSize(self):
        return self.__maxSize

    def setMaxSize(self, newMax):
        if isinstance(newMax, int):
            self.__sem.acquire()
            oldmax = self.__maxSize
            self.__maxSize = newMax
            for index in range(newMax, oldmax):
                key = self.__ordered.pop(index)
                self.pop(key)
            self.__sem.release()
        else:
            EDVerbose.WARNING("ImageCache.setMaxSize: not an Integer %s" % newMax)
    maxSize = property(getMaxSize, setMaxSize)



class EDPluginExecMedianFilterv1_0(EDPluginExec):
    """
    Calculate the median image of a set of images, pixel by pixel. 
    """
    __dictImages = ImageCache()

    def __init__(self):
        """
        """
        EDPluginExec.__init__(self)
        self.setXSDataInputClass(XSDataInputMedianFilter)
        self.images = []
        self.outputImage = None
        self.outputArray = None

    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        EDVerbose.DEBUG("EDPluginExecMedianFilterv1_0.checkParameters")
        self.checkMandatoryParameters(self.getDataInput(), "Data Input is None")
        self.checkMandatoryParameters(self.getDataInput().getInputImages(), "Data Input is None")

    def preProcess(self, _edObject=None):
        EDPluginExec.preProcess(self)
        EDVerbose.DEBUG("EDPluginExecMedianFilterv1_0.preProcess")
        self.images = [ os.path.abspath(i.getPath().getValue()) for  i in  self.getDataInput().getInputImages()]
        if self.getDataInput().getOutputImage() is not None:
            self.outputImage = os.path.abspath(self.getDataInput().getOutputImage().getPath().getValue())


    def process(self, _edObject=None):
        EDPluginExec.process(self)
        EDVerbose.DEBUG("EDPluginExecMedianFilterv1_0.process")
        ndArray3D = None
        for strImgName in self.images:
            if not os.path.isfile(strImgName) :
                EDVerbose.ERROR("Unable to read file %s" % strImgName)
            else:
                if not strImgName in self.__dictImages:
                    data = fabio.open(strImgName).data
                    shape = data.shape
                    self.__dictImages[strImgName] = data.reshape(1, shape[0], shape[1])
                if ndArray3D is None:
                    ndArray3D = self.__dictImages[strImgName]
                else:
                    ndArray3D = numpy.concatenate((ndArray3D, self.__dictImages[strImgName]), axis=0)
        self.outputArray = scipy.median(ndArray3D, axis=0)

    def postProcess(self, _edObject=None):
        EDPluginExec.postProcess(self)
        EDVerbose.DEBUG("EDPluginExecMedianFilterv1_0.postProcess")
        # Create some output data
        xsDataResult = XSDataResultMedianFilter()
        if self.outputImage is None:
            xsDataResult.setOutputArray(EDUtilsArray.arrayToXSData(self.outputArray))
        else:
            edf = fabio.edfimage.edfimage(data=self.outputArray.astype("float32"))
            edf.write(self.outputImage)
            xsDataResult.setOutputImage(XSDataImage(XSDataString(self.outputImage)))

        self.setDataOutput(xsDataResult)
        self.outputArray = None

################################################################################################
###############  Class Ordered dictionary limited in size           ############################
################################################################################################

class ImageCache(dict):
    __sem = threading.Semaphore()
    def __init__(self, maxSize=100):
        dict.__init__(self)
        self.__ordered = []
        self.__maxSize = maxSize
#        self.size = 0

    def __setitem__(self, key, value):
        """x.__setitem__(i, y) <==> x[i]=y"""

        dict.__setitem__(self, key, value)
        self.__sem.acquire()
        if key in self.__ordered:
            index = self.__ordered.index(key)
            self.__ordered.pop(index)
        if len(self) > self.__maxSize:
            firstKey = self.__ordered[ 0 ]
            EDVerbose.DEBUG("Removing file %s from cache" % firstKey)
            dict.pop(self, firstKey)
            self.__ordered = self.__ordered[1:]
        self.__ordered.append(key)
        self.__sem.release()

    def __getitem__(self, key):
        """x.__getitem__(y) <==> x[y]"""
        self.__sem.acquire()
        index = self.__ordered.index(key)
        self.__ordered.pop(index)
        self.__ordered.append(key)
        data = dict.__getitem__(self, key)
        self.__sem.release()
        return data

    def keys(self):
        """ returns the list of keys, ordered"""
        return self.__ordered[:]

    def pop(self, key):
        """remove a key for the dictionary and return it's value"""
        self.__sem.acquire()
        try:
            index = self.__ordered.index(key)
        except Exception:
            raise KeyError
        self.__ordered.pop(index)
        myData = self.imageDict.pop(key)
        self.__sem.release()
        return myData

    def getMaxSize(self):
        return self.__maxSize

    def setMaxSize(self, newMax):
        if isinstance(newMax, int):
            self.__sem.acquire()
            oldmax = self.__maxSize
            self.__maxSize = newMax
            for index in range(newMax, oldmax):
                key = self.__ordered.pop(index)
                self.pop(key)
            self.__sem.release()
        else:
            EDVerbose.WARNING("ImageCache.setMaxSize: not an Integer %s" % newMax)
    maxSize = property(getMaxSize, setMaxSize)

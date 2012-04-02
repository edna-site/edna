# coding: utf8
#
#    Project: Exec plugin: Normalization plugin
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) 2010, European Synchrotron Radiation Facility, Grenoble, France
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
from __future__ import with_statement
__author__ = "Jérôme Kieffer"
__license__ = "GPLv3+"
__copyright__ = "2010, European Synchrotron Radiation Facility, Grenoble, France"
__contact__ = "Jerome.Kieffer@esrf.eu"
__data__ = "08/07/2011"

import os, threading
from EDVerbose                  import EDVerbose
from EDPluginExec               import EDPluginExec
from EDUtilsLibraryInstaller    import EDUtilsLibraryInstaller
from EDFactoryPluginStatic      import EDFactoryPluginStatic
from EDUtilsArray               import EDUtilsArray
from EDUtilsUnit                import EDUtilsUnit
from EDConfiguration            import EDConfiguration
#EDFactoryPluginStatic.loadModule("XSDataNormalizeImage")
from XSDataCommon               import XSDataImageExt, XSDataString, XSPluginItem
from XSDataNormalizeImage       import XSDataInputNormalize, XSDataResultNormalize
from EDAssert                   import EDAssert
from EDUtilsPlatform            import EDUtilsPlatform
from EDShare                    import EDShare
from EDUtilsPath                import EDUtilsPath
from EDThreading import Semaphore

################################################################################
# AutoBuilder for Numpy, PIL and Fabio
################################################################################
architecture = EDUtilsPlatform.architecture
fabioPath = os.path.join(EDUtilsPath.EDNA_HOME, "libraries", "FabIO-0.0.7", architecture)
imagingPath = os.path.join(EDUtilsPath.EDNA_HOME, "libraries", "20091115-PIL-1.1.7", architecture)
numpyPath = os.path.join(EDUtilsPath.EDNA_HOME, "libraries", "20090405-Numpy-1.3", architecture)

EDFactoryPluginStatic.preImport("Image", imagingPath)
numpy = EDFactoryPluginStatic.preImport("numpy", numpyPath, _strMethodVersion="version.version")
fabio = EDFactoryPluginStatic.preImport("fabio", fabioPath)


class EDPluginExecNormalizeImagev1_1(EDPluginExec):
    """
    Plugin that normalizes an image (subtract dark current and divide by flat-field image, taking into account the exposure time)
    
    v1.1 is compatible with EDShare -> lower memory footprint 
    """
    dictDark = {} #Nota: the key is a string: str(exposutTime)
#    listDarkExposure = []
#    listDarkArray = []
    semaphore = Semaphore()
    dtype = None #
    CONF_DTYPE_KEY = "dtype"
    CONF_DTYPE_DEFAULT = "float32"


    def __init__(self):
        """
        Constructor of the plugin
        """
        EDPluginExec.__init__(self)
        self.setXSDataInputClass(XSDataInputNormalize)
        self.listDataArray = []
        self.listDataExposure = []
        self.listDarkArray = []
        self.listDarkExposure = []
        self.listFlatArray = []
        self.listFlatExposure = []
        self.npaNormalized = None
        self.strOutputFilename = None
        self.strOutputShared = None
        self.shape = None

    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        self.DEBUG("EDPluginExecNormalizeImagev1_1.checkParameters")
        self.checkMandatoryParameters(self.getDataInput(), "Data Input is None")


    def configure(self):
        """
        Add the dtype to the configuration file, probably "float32" or "float64"
        """
        EDPluginExec.configure(self)
        self.DEBUG("EDPluginExecNormalizeImagev1_1.configure")
        if self.__class__.dtype is None:
            with self.__class__.semaphore:
                xsPluginItem = self.getConfiguration()
                if (xsPluginItem == None):
                    self.WARNING("EDPluginExecNormalizeImagev1_1.configure: No plugin item defined.")
                    xsPluginItem = XSPluginItem()
                strDtype = EDConfiguration.getStringParamValue(xsPluginItem, self.CONF_DTYPE_KEY)
                if(strDtype == None):
                    self.WARNING("EDPluginExecNormalizeImagev1_1.configure: No configuration parameter found for: %s using default value: %s\n%s"\
                                % (self.CONF_DTYPE_KEY, self.CONF_DTYPE_DEFAULT, xsPluginItem.marshal()))
                    self.__class__.dtype = self.CONF_DTYPE_DEFAULT
                else:
                    self.__class__.dtype = str(strDtype.strip().lower())


    def preProcess(self, _edObject=None):
        EDPluginExec.preProcess(self)
        self.DEBUG("EDPluginExecNormalizeImagev1_1.preProcess")
        sdi = self.getDataInput()
        if sdi.getData() == []:
            strError = "You should either provide at least ONE input filename or an array, you provided: %s" % sdi.marshal()
            self.ERROR(strError)
            self.setFailure()
            raise RuntimeError(strError)
        else:
            for inputData in sdi.getData():
                if inputData.exposureTime is None:
                    self.WARNING("You did not provide an exposure time for DATA... using default: 1")
                    self.listDataExposure.append(1.0)
                else:
                    self.listDataExposure.append(EDUtilsUnit.getSIValue(inputData.exposureTime))
                if inputData.path is not None:
                    strPath = inputData.path.value
                    if os.path.isfile(strPath):
                        self.listDataArray.append(fabio.open(strPath).data)
                    else:
                        strError = "The input file provided for DATA is not a valid file: %s" % strPath
                        self.ERROR(strError)
                        self.setFailure()
                        raise RuntimeError(strError)
                elif inputData.array is not None:
                    self.listDataArray.append(EDUtilsArray.xsDataToArray(inputData.array))
                else:
                    strError = "You should either provide an input filename or an array for DATA, you provided: %s" % inputData.marshal()
                    self.ERROR(strError)
                    self.setFailure()
                    raise RuntimeError(strError)

        for inputFlat in sdi.getFlat():
            if inputFlat.exposureTime is None:
                self.WARNING("You did not provide an exposure time for FLAT... using default: 1")
                expTime = 1.0
            else:
                expTime = EDUtilsUnit.getSIValue(inputFlat.exposureTime)
            self.listFlatExposure.append(expTime)
            if inputFlat.path is not None:
                strPath = inputFlat.path.value
                if os.path.isfile(strPath):
                    self.listFlatArray.append(fabio.open(strPath).data)
                else:
                    strError = "The input file provided for FLAT is not a valid file: %s" % strPath
                    self.ERROR(strError)
                    self.setFailure()
                    raise RuntimeError(strError)
            elif inputFlat.array is not None:
                self.listFlatArray.append(EDUtilsArray.xsDataToArray(inputFlat.array))
            else:
                strError = "You should either provide an input filename or an array for FLAT, you provided: %s" % inputFlat.marshal()
                self.ERROR(strError)
                self.setFailure()
                raise RuntimeError(strError)

        with EDPluginExecNormalizeImagev1_1.semaphore:
            for inputDark in sdi.getDark():
                if inputDark.exposureTime is None:
                    self.WARNING("You did not provide an exposure time for Dark... using default: 1")
                    expTime = 1.0
                else:
                    expTime = EDUtilsUnit.getSIValue(inputDark.exposureTime)
                strMeanDarkKey = "/".join((self.getClassName(), "MeanDark%6.3f" % expTime))
                if strMeanDarkKey not in EDShare:
                    self.listDarkExposure.append(expTime)
                    if inputDark.path is not None:
                        strPath = inputDark.path.value
                        if os.path.isfile(strPath):
                            self.listDarkArray.append(fabio.open(strPath).data)
                        else:
                            strError = "The input file provided for Dark is not a valid file: %s" % strPath
                            self.ERROR(strError)
                            self.setFailure()
                            raise RuntimeError(strError)
                    elif inputDark.array is not None:
                        self.listDarkArray.append(EDUtilsArray.xsDataToArray(inputDark.array))
                    elif inputDark.shared is not None:
                        self.listDarkArray.append(EDShare[inputDark.shared.value])
                    else:
                        strError = "You should either provide an input filename or an array for Dark, you provided: %s" % inputDark.marshal()
                        self.ERROR(strError)
                        self.setFailure()
                        raise RuntimeError(strError)

        if sdi.output is not None:
            if (sdi.output.path is not None):
                self.strOutputFilename = sdi.output.path.value
            elif (sdi.output.shared is not None):
                self.strOutputShared = sdi.output.shared.value
        # else export as array.

        EDAssert.equal(len(self.listDataArray), len(self.listDataExposure), _strComment="number of data images / exposure times ")
        EDAssert.equal(len(self.listFlatArray), len(self.listFlatExposure), _strComment="number of flat images / exposure times ")
        EDAssert.equal(len(self.listDarkArray), len(self.listDarkExposure), _strComment="number of dark images / exposure times ")


    def process(self, _edObject=None):
        EDPluginExec.process(self)
        self.DEBUG("EDPluginExecNormalizeImagev1_1.process")

        #numerator part: 
        fTotalDataTime = 0.0
        self.shape = self.listDataArray[0].shape
        npaSummedData = numpy.zeros(self.shape, dtype=self.dtype)

        for i in range(len(self.listDataArray)):
            fTotalDataTime += self.listDataExposure[i]
            npaSummedData += numpy.maximum(self.listDataArray[i] - self.getMeanDark(self.listDataExposure[i]), 0)
        npaNormalizedData = (npaSummedData / fTotalDataTime).astype(self.dtype)

        #denominator part
        fTotalFlatTime = 0.0
        npaSummedFlat = numpy.zeros(self.shape, dtype=self.dtype)

        for i in range(len(self.listFlatArray)):
            fTotalFlatTime += self.listFlatExposure[i]
            npaSummedFlat += numpy.maximum(self.listFlatArray[i] - self.getMeanDark(self.listFlatExposure[i]), 0)

        npaNormalizedFlat = (npaSummedFlat / fTotalFlatTime).astype(self.dtype)

        self.npaNormalized = npaNormalizedData / numpy.maximum(npaNormalizedFlat, numpy.ones_like(npaNormalizedFlat))
        if self.npaNormalized.dtype != numpy.dtype(self.dtype):
            self.npaNormalized = self.npaNormalized.astype(self.dtype)


    def postProcess(self, _edObject=None):
        EDPluginExec.postProcess(self)
        self.DEBUG("EDPluginExecNormalizeImagev1_1.postProcess")
        xsDataResult = XSDataResultNormalize()
        if self.strOutputFilename is not None:
            self.DEBUG("Writing file %s" % self.strOutputFilename)
            edf = fabio.edfimage.edfimage(data=self.npaNormalized, header={})
            edf.write(self.strOutputFilename)
            xsdo = XSDataImageExt(path=XSDataString(self.strOutputFilename))
        elif self.strOutputShared is not None:
            self.DEBUG("EDShare --> %s" % self.strOutputShared)
            EDShare[ self.strOutputShared] = self.npaNormalized
            xsdo = XSDataImageExt(shared=XSDataString(self.strOutputShared))
        else:
            xsdo = XSDataImageExt(array=EDUtilsArray.arrayToXSData(self.npaNormalized))
        xsDataResult.output = xsdo
        # Create some output data
        self.setDataOutput(xsDataResult)


    def finallyProcess(self, _edObject=None):
        """
        after processing of the plugin:
        remove reference to large objects to save memory
        """
        self.DEBUG("EDPluginExecNormalizeImagev1_1.finallyProcess")
        EDPluginExec.finallyProcess(self, _edObject)
        self.listDataArray = None
        self.listDataExposure = None
        self.listFlatArray = None
        self.listFlatExposure = None
        self.npaNormalized = None


    def getMeanDark(self, _fExposureTime):
        """
        @param _fExposureTime: exposure time 
        @return: mean of darks with this exposure time
        """
        with self.__class__.semaphore:
            if  str(_fExposureTime) not in self.__class__.dictDark:
                npaSumDark = numpy.zeros(self.shape, dtype="float64")
                count = 0
                for fExpTime, npaDark in zip(self.listDarkExposure, self.listDarkArray):
                    if abs(fExpTime - _fExposureTime) / _fExposureTime < 1e-4:
                        npaSumDark += npaDark
                        count += 1
                if count == 0:
                    self.WARNING("No Dark image with Exposure time = %.3f, no dark subtraction" % _fExposureTime)
                    self.__class__.dictDark[str(_fExposureTime) ] = npaSumDark
                else:
                    self.__class__.dictDark[str(_fExposureTime) ] = npaSumDark / float(count)
        return  self.__class__.dictDark[str(_fExposureTime)]


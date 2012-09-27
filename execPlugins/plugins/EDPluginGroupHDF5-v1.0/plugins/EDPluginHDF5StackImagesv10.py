# coding: utf8
#
#    Project: Exec Plugin: HDF5 writers
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) ESRF Grenoble
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
__contact__ = "jerome.kieffer@esrf.eu"
__license__ = "GPLv3+"
__copyright__ = "ESRF Grenoble"
__date__ = "2011-07-26"

###############################################################################
# BIG FAT WARNING
# HDF5 does not like unicode string and crashes with cryptic error messages
###############################################################################
import os
import posixpath
from EDAssert                   import EDAssert
from EDPluginHDF5               import EDPluginHDF5
from XSDataHDF5v1_0             import XSDataInputHDF5StackImages, XSDataResultHDF5StackImages
from XSDataCommon               import XSDataFile, XSDataString, XSDataImageExt
from EDUtilsArray               import EDUtilsArray
from EDConfiguration            import EDConfiguration
from EDFactoryPluginStatic      import EDFactoryPluginStatic
from EDPluginHDF5               import numpyPath, h5pyPath
numpy = EDFactoryPluginStatic.preImport("numpy", numpyPath, _strMethodVersion="__version__")
h5py = EDFactoryPluginStatic.preImport("h5py", h5pyPath, _strMethodVersion="version.version")


class EDPluginHDF5StackImagesv10(EDPluginHDF5):
    """
    This plugin is made for putting together many images in a 3D cube as a stack of images, 
    and put them together in an NeXus/HDF5 file
    """
    HDF5_GROUP_HEADERS = "headers"
    HDF5_DATASET_IMAGE_FILENAMES = "filenames"
    HDF5_DATASET_STACKIMAGE_ATTRIBUTES = {#"creator":"EDNA",
#                               "NX_class":"NXdata",
                               "interpretation": "image", # "spectrum", "scalar", "image" or "vertex"
                               "signal":"1",
                               }


    def __init__(self):
        """
        """
        EDPluginHDF5.__init__(self)
        self.setXSDataInputClass(XSDataInputHDF5StackImages)
        self.strHDF5Filename = None
        self.listImageFilenames = []
        self.listForcedPositions = []
        self.listImageDates = []
        self.listArray = []
        self.bDeleteImage = False
        self.hdf5group = None #Name of the group(directory) where we will work


    def preProcess(self, _edObject=None):
        EDPluginHDF5.preProcess(self)
        self.DEBUG("EDPluginHDF5StackImagesv10.preProcess")

        for onefile in self.dataInput.inputImageFile:
            if onefile is None:
                self.ERROR("Please investigate why  EDPluginHDF5StackImagesv10.dataInput.inputImageFile is a list containing None !!!!")
                self.setFailure()
                continue
            if onefile.path is not None:
                self.listImageFilenames.append(onefile.path.value)
            if onefile.date is not None:
                self.listImageDates.append(onefile.date.value)
            if onefile.number is not None:
                self.listForcedPositions.append(onefile.number.value)
            self.listArray.append(EDUtilsArray.getArray(onefile))

        for oneArray in self.dataInput.inputArray:
            self.listArray.append(EDUtilsArray.xsDataToArray(oneArray))

        if self.dataInput.index != []:
            self.listForcedPositions = [i.value for i in self.dataInput.index]

        if self.dataInput.getDeleteInputImage() is not None:
            self.bDeleteImage = bool(self.dataInput.deleteInputImage.value)

        if self.listForcedPositions != []:
            EDAssert.equal(len(self.listForcedPositions), max(len(self.listImageFilenames), len(self.listArray)), "Forced position list has a good length")
        if self.listImageDates != []:
            EDAssert.equal(len(self.listImageDates) , len(self.listImageFilenames), "listImageDates has the same size as listImageFilenames")

        self.hdf5group = EDPluginHDF5.createStructure(self.strHDF5Filename, self.strHDF5Path, self.dictExtraAttributes)


    def process(self, _edObject=None):
        EDPluginHDF5.process(self)
        self.DEBUG("EDPluginHDF5StackImagesv10.process")
        length = len(self.listForcedPositions)
        if length == 0:
            for oneFilename in self.listImageFilenames:
                header, data = self.readImage(oneFilename)
                self.DEBUG("Writing image %s on top of the stack" % (oneFilename))
                self.processOneImage(data, position=None, filename=oneFilename, dictHeaders=header)
            for oneArray in self.listArray:
                self.DEBUG("Writing image from array on top of the stack")
                self.processOneImage(oneArray)
        else:
            if len(self.listImageFilenames) == length :
                for i in xrange(length):
                    self.DEBUG("Writing image %s at position %i" % (self.listImageFilenames[i], self.listForcedPositions[i]))
                    header, data = self.readImage(self.listImageFilenames[i])
                    self.processOneImage(data, position=self.listForcedPositions[i], filename=self.listImageFilenames[i], dictHeaders=header)
            elif len(self.listArray) == length:
                for i in xrange(length):
                    self.DEBUG("Writing image from array at position %i" % (self.listForcedPositions[i]))
                    self.processOneImage(self.listArray[i], self.listForcedPositions[i])


    def postProcess(self, _edObject=None):
        EDPluginHDF5.postProcess(self)
        self.DEBUG("EDPluginHDF5StackImagesv10.postProcess")
        xsDataResult = XSDataResultHDF5StackImages()
        if os.path.isfile(self.strHDF5Filename):
            xsDataFile = XSDataFile(path=XSDataString(value=self.strHDF5Filename))
            xsDataResult.setHDF5File(xsDataFile)
            xsDataResult.setInternalHDF5Path(XSDataString(self.strHDF5Path))
        self.setDataOutput(xsDataResult)

        # Delete input images if requested
        if self.bDeleteImage:
            for oneImage in self.listImageFilenames:
                os.remove(oneImage)

        #De-allocate memory no more used.
        self.listImageFilenames = []
        self.listForcedPositions = []
        self.listImageDates = []
        self.listArray = []



    def processOneImage(self, npaArray, position=None, filename=None, dictHeaders=None):
        """
        This is the treatment of one image

        @param npaArray: array representing the image 
        @type npaArray: 2 dimension numpy array   
        @param position: the position of the image in the HDF5 dataset. If None just append at the top of the stack.
        @type position: integer         
        @param filename: the name of the input image, could be useful for loggiing ...
        @type filename: string
        @param dictHeaders:  header of the EDF-like file to put to the "headers" subgroup. 
        @type dictHeaders: dictionary
        """

        self.DEBUG("EDPluginHDF5StackImagesv10.processOneImage: file %s at position %s" % (filename, position))
        if dictHeaders is None:
            dictHeaders = {}
        if (self.dtype is not None) and (numpy.dtype(self.dtype) != npaArray.dtype):
            npaArray = npaArray.astype(self.dtype)
        iMaxSize = 0
        dSizeOfDataSets = {} #key=h5path, value=int:len of dataset 
        with self.__class__.getFileLock(self.strHDF5Filename):
#        self.lockFile(self.strHDF5Filename)
    ################################################################################
    # Read all the sizes of all datasets
    ################################################################################
            for oneItem in self.hdf5group:
                if oneItem == self.HDF5_DATASET_DATA:
                    dataset = self.hdf5group[oneItem]
                    if "HDF5 dataset" in str(dataset):
                        size = dataset.len()
                        dSizeOfDataSets[oneItem] = size
                        if (size > iMaxSize):
                            iMaxSize = size
                elif oneItem == self.HDF5_DATASET_IMAGE_FILENAMES:
                    dataset = self.hdf5group[oneItem]
                    if "HDF5 dataset" in str(dataset):
                        size = dataset.len()
                        dSizeOfDataSets[oneItem] = size
                        if (size > iMaxSize):
                            iMaxSize = size
                elif oneItem == self.HDF5_GROUP_HEADERS:
                    subgroup = self.hdf5group[oneItem]
                    if "HDF5 group" in str(subgroup):
                        for oneHeader in self.hdf5group[oneItem]:
                            path = posixpath.join(oneItem, oneHeader)
                            subdataset = self.hdf5group[path]
                            if "HDF5 dataset" in str(subdataset):
                                size = subdataset.len()
                                dSizeOfDataSets[path] = size
                                if (size > iMaxSize):
                                    iMaxSize = size
            if position is not None:
                iMaxSize = position


    ################################################################################
    # Treatement of the filenames
    ################################################################################
            if filename is not None:
                if self.HDF5_DATASET_IMAGE_FILENAMES not in dSizeOfDataSets:
                    filenames = self.hdf5group.create_dataset(self.HDF5_DATASET_IMAGE_FILENAMES,
                                                              (iMaxSize + 1,), h5py.special_dtype(vlen=str), maxshape=(None,))
                else:
                    filenames = self.hdf5group[self.HDF5_DATASET_IMAGE_FILENAMES]
                if filenames.len() < iMaxSize + 1:
                    filenames.resize((iMaxSize + 1,))
                if isinstance(filename, unicode):
                    myFilename = os.path.basename(filename).encode(EDPluginHDF5StackImagesv10.ENCODING)
                else:
                    myFilename = os.path.basename(filename)
                self.DEBUG("position %i filename %s type %s" % (iMaxSize, myFilename, type(myFilename)))
                filenames[iMaxSize] = myFilename
                if self.HDF5_DATASET_IMAGE_FILENAMES in dSizeOfDataSets:
                    dSizeOfDataSets.pop(self.HDF5_DATASET_IMAGE_FILENAMES)

    ################################################################################
    #   Treatement of all metadata, stored in datasets of strings (numpy array of strings) 
    ################################################################################
            if dictHeaders:
                self.hdf5group.require_group(self.HDF5_GROUP_HEADERS)
            for oneMetaData in dictHeaders:
                myMetaData = dictHeaders[oneMetaData]
                path = self.HDF5_GROUP_HEADERS + "/" + oneMetaData
                self.DEBUG("position %i internal path  %s type %s" % (iMaxSize, path, type(path)))
                if not dSizeOfDataSets.has_key(path):
                    if isinstance(myMetaData, str):
                        oneMetaDataset = self.hdf5group.create_dataset(path, shape=(iMaxSize + 1,), dtype=h5py.special_dtype(vlen=str), maxshape=(None,))
                    if isinstance(myMetaData, int):
                        oneMetaDataset = self.hdf5group.create_dataset(path, shape=(iMaxSize + 1,), dtype="int", maxshape=(None,))
                    if isinstance(myMetaData, float):
                        oneMetaDataset = self.hdf5group.create_dataset(path, shape=(iMaxSize + 1,), dtype="float", maxshape=(None,))
                else:
                    oneMetaDataset = self.hdf5group[path]

                if oneMetaDataset.len() < iMaxSize + 1:
                    oneMetaDataset.resize((iMaxSize + 1,))
                oneMetaDataset[iMaxSize] = myMetaData

                if path in dSizeOfDataSets:
                    dSizeOfDataSets.pop(path)

    ################################################################################
    # END of metadata treatment 
    ################################################################################
    # Start of data treatment
    ################################################################################
            dataset = None
            if self.HDF5_DATASET_DATA in self.hdf5group:
                dataset = self.hdf5group[self.HDF5_DATASET_DATA]
                if isinstance(dataset, h5py.highlevel.Dataset)\
                and (dataset.shape[-2:] == npaArray.shape[-2:]) \
                and (dataset.dtype == npaArray.dtype) :
                    self.DEBUG("dataset exists and is good")
                    dataset = self.hdf5group[self.HDF5_DATASET_DATA]
                else:
                    self.DEBUG("dataset exists and is BAD %s %s" % (dataset.dtype, npaArray.dtype))
                    dataset = None
                    del self.hdf5group[self.HDF5_DATASET_DATA]
            if dataset is None:
                shape = ((iMaxSize + 1),) + npaArray.shape
                maxshape = (None,) + npaArray.shape
                chunksize = (1, max(1, npaArray.shape[0] // self.iChunkSegmentation)) + npaArray.shape[1:]
                self.DEBUG("dataset creation shape= %s maxshape=%s type=%s" % (shape, maxshape, npaArray.dtype))

                dataset = self.hdf5group.create_dataset(self.HDF5_DATASET_DATA,
                              shape=shape, dtype=npaArray.dtype, maxshape=maxshape,
                              compression=self.HDF5_Compression,
                              chunks=chunksize)

                for key in self.HDF5_DATASET_ATTRIBUTES:
                    if not key in dataset.attrs:
                        dataset.attrs.create(key, self.HDF5_DATASET_ATTRIBUTES[key])
                for key in self.HDF5_DATASET_STACKIMAGE_ATTRIBUTES:
                    if not key in dataset.attrs:
                        dataset.attrs.create(key, self.HDF5_DATASET_STACKIMAGE_ATTRIBUTES[key])
                if dataset.name in self.dictExtraAttributes:
                    for key in self.dictExtraAttributes[dataset.name]:
                        if key not in dataset.attrs:
                            dataset.attrs.create(key, self.dictExtraAttributes[dataset.name][key])

            if dataset.len() < (iMaxSize + 1):
                dataset.resize((iMaxSize + 1,) + npaArray.shape)

            dataset[iMaxSize, :, :] = npaArray
            if self.HDF5_DATASET_DATA in dSizeOfDataSets:
                dSizeOfDataSets.pop(self.HDF5_DATASET_DATA)

    ################################################################################
    # END of data teatement
    ################################################################################
            #     And finally we append white space at the end (or reset)  when no metadata keys were in the input file.        
            for oneItem in dSizeOfDataSets:
                self.DEBUG("Warning probably un-consistent dataset for " + oneItem)
                oneMetaDataset = self.hdf5group[oneItem]
                if oneMetaDataset.len() < iMaxSize + 1:
                    oneMetaDataset.resize((iMaxSize + 1,))
                else:
                    if isinstance(h5py.check_dtype(vlen=oneMetaDataset.dtype), str):
                        oneMetaDataset[iMaxSize] = ""
                    else:
                        oneMetaDataset[iMaxSize] = 0
#        self.releaseFile(self.strHDF5Filename)



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


class EDPluginHDF5StackImagesv10test(EDPluginHDF5):
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
        self.DEBUG("EDPluginHDF5StackImagesv10test.preProcess")

        for onefile in self.dataInput.inputImageFile:
            if onefile.path is not None:
                self.listImageFilenames.append(onefile.path.value)
            if onefile.date is not None:
                self.listImageDates.append(onefile.date.value)
            if onefile.number is not None:
                self.listForcedPositions.append(onefile.number.value)
            self.listArray.append(EDUtilsArray.getArray(onefile))

        for oneArray in self.dataInput.getInputArray():
            self.listArray.append(EDUtilsArray.xsDataToArray(oneArray))

        if self.dataInput.index != []:
            self.listForcedPositions = [i.value for i in self.dataInput.index]

        if self.dataInput.getDeleteInputImage() is not None:
            self.bDeleteImage = bool(self.dataInput.deleteInputImage.value)

        if self.listForcedPositions != []:
            EDAssert.equal(len(self.listForcedPositions), max(len(self.listImageFilenames), len(self.listArray)), "Forced position list has a good length")
        if self.listImageDates != []:
            EDAssert.equal(len(self.listImageDates) , len(self.listImageFilenames), "listImageDates has the same size as listImageFilenames")

#        self.hdf5group = EDPluginHDF5.createStructure(self.strHDF5Filename, self.strHDF5Path, self.dictExtraAttributes)


    def process(self, _edObject=None):
        EDPluginHDF5.process(self)
        self.DEBUG("EDPluginHDF5StackImagesv10test.process")
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
        self.DEBUG("EDPluginHDF5StackImagesv10test.postProcess")
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
        if dictHeaders is None:
            dictHeaders = {}
        f = fabio.edfimage.edfimage(data=npaArray, header=dictHeaders)
        f.write("%s_%s_%s_%s.edf" % (self.strHDF5Filename, self.strHDF5Path, filename, position))

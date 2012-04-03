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
__date__ = "2011-05-11"


###############################################################################
# BIG FAT WARNING
# HDF5 does not like unicode string and crashes with cryptic error messages
###############################################################################

import os, threading, time, locale
from EDVerbose                  import EDVerbose
from EDPluginHDF5               import EDPluginHDF5
from EDAssert                   import EDAssert
from EDUtilsPlatform            import EDUtilsPlatform
from XSDataHDF5v1_0             import XSDataInputHDF5MapSpectra, XSDataResultHDF5MapSpectra
from XSDataCommon               import XSDataFile, XSDataString
from EDConfiguration            import EDConfiguration
from EDUtilsArray               import EDUtilsArray
from EDFactoryPluginStatic      import EDFactoryPluginStatic
from EDPluginHDF5               import numpyPath, h5pyPath, fabioPath
numpy = EDFactoryPluginStatic.preImport("numpy", numpyPath, _strMethodVersion="__version__")
h5py = EDFactoryPluginStatic.preImport("h5py", h5pyPath, _strMethodVersion="version.version")
fabio = EDFactoryPluginStatic.preImport("fabio", fabioPath, _strMethodVersion="version")



class EDPluginHDF5MapOfSpectrav10(EDPluginHDF5):
    """
    This plugin is made for putting together 1D spectra comming from a 2D scan  in a 3D cube, 
    read using various libraries ... , and put them together in an NeXus/HDF5 file
    """
    HDF5_DATASET_MAPSPECTRA_ATTRIBUTES = {"interpretation": "spectrum", # "spectrum", "scalar", "image" or "vertex"
                                               "signal":"1",
                                               }

    def __init__(self):
        """
        """
        EDPluginHDF5.__init__(self)
        self.setXSDataInputClass(XSDataInputHDF5MapSpectra)
        self.listSpectrumFilenames = []
        self.listForcedPositions = []
        self.listSpectrumFileType = []
        self.listArray = []
        self.meshScan = {"FastMotorSteps":0,
                       "FastMotorStart":0,
                       "FastMotorStop":0,
                       "SlowMotorSteps":0,
                       "SlowMotorStart":0,
                       "SlowMotorStop":0, }
        self.bDeleteSpectrum = False



    def preProcess(self, _edObject=None):
        EDPluginHDF5.preProcess(self)
        self.DEBUG("EDPluginHDF5MapOfSpectrav10.preProcess")

        for oneSpectrum in self.getDataInput().getInputSpectrumFile():
            if oneSpectrum.getPath() is not None:
                strFileName = oneSpectrum.getPath().getValue()
                self.DEBUG("getInputSpectrumFile: %s" % strFileName)
                self.listSpectrumFilenames.append(strFileName)
            elif oneSpectrum.getArray() is not None:
                self.DEBUG("getInputArray: %s" % strFileName)
                self.listArray.append(EDUtilsArray.xsDataToArray())
            else:
                self.ERROR("A spectrum should either contain an image file or an array.")
                self.setFailure()
                raise
            if (oneSpectrum.getFastMotorPosition() is not None) and (oneSpectrum.getSlowMotorPosition() is not None):
                self.listForcedPositions.append({"Slow":oneSpectrum.getSlowMotorPosition().getValue(),
                                                 "Fast":oneSpectrum.getFastMotorPosition().getValue()})
            if oneSpectrum.getFileType() is not None:
                self.listSpectrumFileType.append(oneSpectrum.getFileType.getValue())
            if oneSpectrum.getMeshScan() is not None:
                XSDMesh = oneSpectrum.getMeshScan()
#                self.DEBUG(XSDMesh.marshal())
                self.meshScan["FastMotorSteps"] = XSDMesh.getFastMotorSteps().getValue()
                self.meshScan["FastMotorStart"] = XSDMesh.getFastMotorStart().getValue()
                self.meshScan["FastMotorStop" ] = XSDMesh.getFastMotorStop().getValue()
                self.meshScan["SlowMotorSteps"] = XSDMesh.getSlowMotorSteps().getValue()
                self.meshScan["SlowMotorStart"] = XSDMesh.getSlowMotorStart().getValue()
                self.meshScan["SlowMotorStop" ] = XSDMesh.getSlowMotorStop().getValue()
                self.DEBUG("MeshScan= %s" % self.meshScan)
        if self.getDataInput().getDeleteInputSpectrum() is not None:
            if self.getDataInput().getDeleteInputSpectrum() in [True, "true", "True", 1, "1"]:
                self.bDeleteSpectrum = True

        if len(self.listForcedPositions) > 0  :
            EDAssert.equal(len(self.listForcedPositions), max(len(self.listSpectrumFilenames), len(self.listArray)), _strComment="list of forced position has the right size")

        self.hdf5group = self.createStructure(self.strHDF5Filename, self.strHDF5Path, self.dictExtraAttributes)


    def process(self, _edObject=None):
        EDPluginHDF5.process(self)
        self.DEBUG("EDPluginHDF5MapOfSpectrav10.process")
        maxSize = (((self.meshScan["SlowMotorSteps" ]), (self.meshScan["FastMotorSteps" ])))

        for filename in self.listSpectrumFilenames:
            self.listArray.append(fabio.open(filename).data)

        if self.listForcedPositions == []:
            for oneArray in self.listArray:
                self.processOneSpectrum(oneArray, position=maxSize, maxSize=maxSize)
        else:
            for i in range(len(self.listForcedPositions)):
                fSlowPosition = (self.listForcedPositions[i]["Slow"] - self.meshScan["SlowMotorStart"]) / \
                            (self.meshScan["SlowMotorStop"] - self.meshScan["SlowMotorStart"]) * \
                            (self.meshScan["SlowMotorSteps" ])
                fFastPosition = (self.listForcedPositions[i]["Fast"] - self.meshScan["FastMotorStart"]) / \
                            (self.meshScan["FastMotorStop"] - self.meshScan["FastMotorStart"]) * \
                               (self.meshScan["FastMotorSteps" ])
                self.processOneSpectrum(self.listArray[i], (int(round(fSlowPosition)), int(round(fFastPosition))), maxSize=maxSize)


    def postProcess(self, _edObject=None):
        EDPluginHDF5.postProcess(self)
        self.DEBUG("EDPluginHDF5MapOfSpectrav10.postProcess")
        xsDataResult = XSDataResultHDF5MapSpectra()
        if os.path.isfile(self.strHDF5Filename):
            xsDataFile = XSDataFile()
            xsDataFile.setPath(XSDataString(self.strHDF5Filename))
            xsDataResult.setHDF5File(xsDataFile)
            xsDataResult.setInternalHDF5Path(XSDataString(self.strHDF5Path))
        self.setDataOutput(xsDataResult)

        # Delete input images if requested
        if self.bDeleteSpectrum:
            for oneImage in self.listSpectrumFilenames:
                os.remove(oneImage)
#        De-Allocate memory
        self.listSpectrumFilenames = []
        self.listForcedPositions = []
        self.listSpectrumFileType = []
        self.listArray = []


    def processOneSpectrum(self, npaImage, position, maxSize=None):
        """
        This is the treatment of one spectrum including the creation of the NXData structure 
        
        @param npaImage: the numpy array containing the spectrum
        @type npaImage: numpy array.
        @param position: the position of the image in the HDF5 dataset
        @type position: 2-tuple of integer
        @param maxSize: the size of the mesh 
        @type maxSize: 2-tuple of integer
         
        """
        self.DEBUG("EDPluginHDF5MapOfSpectrav10.processOneImage: position %s with shape %s" % (position, maxSize))
        listMaxSize = [0, 0, npaImage.shape[-1]]
        if maxSize is not None and isinstance(maxSize, (list, tuple)):
            listMaxSize[0] = max(maxSize[0], 1 + position[0])
            listMaxSize[1] = max(maxSize[1], 1 + position[1])
        if position[0] < 0: position = (0, position[1])
        if position[1] < 0: position = (position[0], 0)
        with self.getFileLock(self.strHDF5Filename):

    ################################################################################
    # Read all the sizes of all datasets
    ################################################################################
            dataset = None
            for oneItem in self.hdf5group:
                if oneItem == self.HDF5_DATASET_DATA:
                    dataset = self.hdf5group[oneItem]
                    if "HDF5 dataset" in str(dataset):
                        for i in range(3):
                            if dataset.shape[i] > listMaxSize[i]:
                                listMaxSize[i] = dataset.shape[i]
                        self.DEBUG("dataset exists and listMaxSize is " + str(listMaxSize))

    ################################################################################
    # Start of data treatement
    ################################################################################

            if dataset is not None:
                if (dataset.shape[-1] == npaImage.shape[-1]) and (dataset.dtype == npaImage.dtype) :
                    self.DEBUG("dataset exists and is good")
                else:
                    self.DEBUG("dataset exists and is BAD %s %s, reseting" % (dataset.dtype, npaImage.dtype))
                    dataset = None
                    del self.hdf5group[self.HDF5_DATASET_DATA]
            else:
                shape = ((listMaxSize[0] + 1), (listMaxSize[1] + 1), npaImage.shape[-1])
                maxshape = (None, None, npaImage.shape[-1])
                chunksize = (1, 1, max(1, npaImage.shape[-1] // self.iChunkSegmentation))
                self.DEBUG("dataset creation shape= %s maxshape=%s type=%s" % (shape, maxshape, npaImage.dtype))
                dataset = self.hdf5group.create_dataset(self.HDF5_DATASET_DATA,
                              shape=shape, dtype=npaImage.dtype, maxshape=maxshape,
                              compression=self.HDF5_Compression, chunks=chunksize)
                for key in self.HDF5_DATASET_ATTRIBUTES:
                    if key not in dataset.attrs:
                        dataset.attrs.create(key, self.HDF5_DATASET_ATTRIBUTES[key])
                for key in self.HDF5_DATASET_MAPSPECTRA_ATTRIBUTES:
                    if not key in dataset.attrs:
                        dataset.attrs.create(key, self.HDF5_DATASET_MAPSPECTRA_ATTRIBUTES[key])
                if dataset.name in self.dictExtraAttributes:
                    for key in self.dictExtraAttributes[dataset.name]:
                        if key not in dataset.attrs:
                            dataset.attrs.create(key, self.dictExtraAttributes[dataset.name][key])

                nxgroup = self.hdf5group.require_group(self.HDF5_DATAGROUP_NXDATA)
                nxgroup.attrs.create("NX_class", "NXdata")
                if not self.HDF5_DATASET_DATA in nxgroup:
                    nxgroup[self.HDF5_DATASET_DATA] = dataset #h5py.SoftLink(self.hdf5group.name + "/" + self.HDF5_DATASET_DATA)
                if not self.HDF5_DATASET_START_TIME in self.hdf5group:
                    self.hdf5group[self.HDF5_DATASET_START_TIME] = self.getIsoTime()
            if self.HDF5_DATASET_END_TIME in self.hdf5group:
                del self.hdf5group[self.HDF5_DATASET_END_TIME]
            self.hdf5group[self.HDF5_DATASET_END_TIME] = self.getIsoTime()

            self.DEBUG("Test the sizes shape: %s \tlistMaxSize = %s" % (dataset.shape, listMaxSize))
            reshape = False
            for i in xrange(2):

                if dataset.shape[i] < listMaxSize[i]:
                    reshape = True

            if reshape:
                self.DEBUG("Reshape of the dataset to " + str((listMaxSize[0]  , (listMaxSize[1]), +npaImage.shape[-1])))
                dataset.resize((listMaxSize[0] , listMaxSize[1] , npaImage.shape[-1]))

            dataset[position] = npaImage[-1]
            self.DEBUG("End of data treatment on position %s :" % listMaxSize)
    ################################################################################
    # END of data teatement
    ################################################################################


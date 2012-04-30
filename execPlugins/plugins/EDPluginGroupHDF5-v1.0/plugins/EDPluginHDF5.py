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
__date__ = "2012-03-12"

###############################################################################
# BIG FAT WARNING
# HDF5 does not like unicode string and crashes with cryptic error messages
###############################################################################

import os, time, locale

from EDVerbose                  import EDVerbose
from EDPlugin                   import EDPlugin
from EDUtilsPlatform            import EDUtilsPlatform
from EDConfiguration            import EDConfiguration
from EDFactoryPlugin            import edFactoryPlugin  as EDFactoryPluginStatic
from EDDecorator                import deprecated
from EDThreading                import Semaphore
from EDUtilsPath                import EDUtilsPath
architecture = EDUtilsPlatform.architecture
numpyPath = os.path.join(EDUtilsPath.EDNA_HOME, "libraries", "20090405-Numpy-1.3", architecture)
h5pyPath = os.path.join(EDUtilsPath.EDNA_HOME, "libraries", "H5Py-1.3.0", architecture)
fabioPath = os.path.join(EDUtilsPath.EDNA_HOME, "libraries", "FabIO-0.0.7", architecture)
imagingPath = os.path.join(EDUtilsPath.EDNA_HOME, "libraries", "20091115-PIL-1.1.7", architecture)

numpy = EDFactoryPluginStatic.preImport("numpy", numpyPath, _strMethodVersion="__version__")
h5py = EDFactoryPluginStatic.preImport("h5py", h5pyPath, _strMethodVersion="version.api_version", _strForceVersion="1.8")
Image = EDFactoryPluginStatic.preImport("Image", imagingPath, _strMethodVersion="VERSION")
fabio = EDFactoryPluginStatic.preImport("fabio", fabioPath, _strMethodVersion="version")

if h5py is None:
    EDVerbose.error("h5py is None ... please investigate why !!!")
    EDVerbose.writeErrorTrace()
#    raise ImportError("EDPluginHDF5 cannot work without h5py !!!")


if "EDNA_SITE" not in os.environ:
    os.environ["EDNA_SITE"] = "edna-site"


class EDPluginHDF5(EDPlugin):
    """
    This is a common part for all EDNA plugin writing HDF5. most methods are class methods 
    """
    __semCls = Semaphore()
    __dictHDF5 = {} #key: filename, value: hdf5 h5py objects
    __dictLock = {} #key: filename, value:semaphores for writing
    __bConfigured = False
    HDF5_Multifiles = False
    HDF5_Compression = None
    CONF_COMPRESSION_KEY = "compression"
    ENCODING = max("ASCII", locale.getdefaultlocale()[1])
#    if ENCODING is None: ENCODING = "ASCII"
    HDF5_ROOT_ATTRIBUTES = {#"NeXus_version":"4.3.0",
                            #"HDF5_Version":h5py.version.hdf5_version,
                            "HDF5_API_Version":h5py.version.api_version,
                            "encoding":ENCODING,
                            "source":os.environ["EDNA_SITE"],
                            "creator":"EDNA",
#                            "NX_class":"NXroot",
                            }
    HDF5_GROUP_ATTRIBUTES = {"creator":"EDNA",
                             #"NX_class":"NXentry",
                             #"Class":"Spectra"
                             }
    NX_GROUP_ATTRIBUTES = {"NX_class":"NXentry"}
    HDF5_DATASET_ATTRIBUTES = {"creator":"EDNA",
#                               "NX_class":"NXdata",
                               #"interpretation": "spectrum", #Could be "scalar", "image" or "vertex"
                               #"signal":"1",
                               }
    HDF5_DATAGROUP_NXDATA = "NXdata"
    HDF5_DATASET_DATA = "data"
    HDF5_DATASET_START_TIME = "start_time"
    HDF5_DATASET_END_TIME = "end_time"


    def __init__(self):
        """
        Constructor of EDPluginHDF5
        """
        super(EDPluginHDF5, self).__init__()
        self.strHDF5Filename = None
        self.strHDF5Path = None
        self.dtype = None
        self.dictExtraAttributes = {} #key= h5path, value dict of attributes
        self.__iChunkSegmentation = 1

    def get(self, h5Path, default):
        try:
            self.__getitem__(h5Path)
        except KeyError:
            return default

    def __getitem__(self, item):
        """
        implements a getter a la dictionnary but compatible with  
        """
        if self.strHDF5Filename in self.__dictLock:
            return  self.__dictHDF5[item]
        else:
            raise KeyError("HDF5 file %s not under control of EDPluginHDF5" % self.strHDF5Filename)


    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        super(EDPluginHDF5, self).checkParameters()
        self.DEBUG("EDPluginHDF5.checkParameters")
        self.checkMandatoryParameters(self.dataInput, "Data Input is None")
        self.checkMandatoryParameters(self.dataInput.HDF5File, "No HDF5 file provided")
        self.checkMandatoryParameters(self.dataInput.internalHDF5Path, "No HDF5 internal path provided")


    def configure(self):
        """
        Configure the HDF5 compression scheme
        """
        super(EDPluginHDF5, self).configure()
        self.DEBUG("EDPluginHDF5.configure")
        if not EDPluginHDF5.__bConfigured:
            xsPluginItem = self.getConfiguration()
            if xsPluginItem is not None:
                strCompression = EDConfiguration.getStringParamValue(xsPluginItem, EDPluginHDF5.CONF_COMPRESSION_KEY)
                if strCompression != None:
                    if strCompression == "None":
                        EDPluginHDF5.HDF5_Compression = None
                    else:
                        EDPluginHDF5.HDF5_Compression = strCompression
            EDPluginHDF5.__bConfigured = True


    def preProcess(self, _edObject=None):
        super(EDPluginHDF5, self).preProcess()
        self.DEBUG("EDPluginHDF.preProcess")
        self.strHDF5Filename = self.dataInput.HDF5File.path.value
        self.strHDF5Path = self.dataInput.internalHDF5Path.value

        if self.dataInput.multiFiles is not None:
            if self.dataInput.multiFiles.value:
                base, ext = os.path.splitext(self.strHDF5Filename)
                self.strHDF5Filename = base + "%04d" + ext
                self.HDF5_Multifiles = True

        if self.dataInput.forceDtype is not None:
            self.dtype = self.dataInput.forceDtype.value
        for extraAttr in self.dataInput.extraAttributes:
            attr = {}
            h5path = extraAttr.h5path.value
            for meta in extraAttr.metadata.keyValuePair:
                attr[meta.key.value] = meta.value.value
            self.dictExtraAttributes[h5path] = attr
        if self.dataInput.chunkSegmentation is not None:
            self._iChunkSegmentation = self.dataInput.chunkSegmentation.value

    def postProcess(self, _edObject=None):
        self.DEBUG("EDPluginHDF5.postProcess")
        super(EDPluginHDF5, self).postProcess()
        if self.isVerboseDebug():
            self.flush(self.strHDF5Filename)

    @classmethod
    def readImage(cls, filename):
        """
        Use fabio to load the image and the metadata
        @param filename: name of the file to open
        @type filename: string
        @return: headers, data
        @rtype: 2-tuple (dict,numpyArray)
        """
        fabioImage = fabio.open(filename)
        npaImage = fabioImage.data
        dictMetadata = {}
        for oneMetaData in fabioImage.getheader():
            myMetaData = fabioImage.getheader()[oneMetaData]
            try:
                oneMetaData = oneMetaData.encode(cls.ENCODING)
            except UnicodeDecodeError:
                pass
            try:
                myMetaData = myMetaData.encode(cls.ENCODING)
            except (AttributeError, UnicodeDecodeError):
                myMetaData = fabioImage.getheader()[oneMetaData]
            oneMetaData = oneMetaData.replace("/", "&frasl;")
            dictMetadata[oneMetaData] = myMetaData
        return dictMetadata, npaImage


    @classmethod
    def createStructure(cls, filename, h5path, dictAttributes=None):
        """
        Create an empty HDF5 file with a NeXus structure and return the group to work with.
         
        @param filename: path of the file to be created (just the groups, not the dataset) 
        @type filename: string
        @param h5path: path of the internal NeXus structure to be created
        @type  h5path: string
        @param dictAttributes: dictionary containing h5path: attributes, attributes being a dict
        @type dictAttributes: dictionary (string -> dictionary(string:string)) 
        @rtype: h5py group like
        @return: the h5py implementation of the HDF5 group
        """
        EDVerbose.DEBUG("EDPluginHDF5.createStructure:  HDF5 file %s %s with internal structure %s %s" % (filename, filename.__class__, h5path, h5path.__class__))
        if dictAttributes is None:
            dictAttributes = {}
        if isinstance(filename, unicode):
            filename = filename.encode(cls.ENCODING)
        if isinstance(h5path, unicode):
            h5path = h5path.encode(cls.ENCODING)
        EDVerbose.DEBUG("Creation of HDF5 file %s %s with internal structure %s %s" % (filename, filename.__class__, h5path, h5path.__class__))
        if not os.path.isdir(os.path.dirname(filename)):
                os.makedirs(os.path.dirname(filename))

        with cls.__semCls:
            if not cls.__dictHDF5.has_key(filename):

                if cls.HDF5_Multifiles:
                    try:
                        cls.__dictHDF5[filename] = h5py.File(filename, driver="family")
                    except Exception:
                        EDVerbose.ERROR("Error in EDPluginHDF5.createStructure during opening HDF5 multi-file " + filename)
                        raise
                else:
                    try:
                        cls.__dictHDF5[filename] = h5py.File(filename)
                    except Exception:
                        EDVerbose.ERROR("Error in EDPluginHDF5.createStructure during opening HDF5 file %s" % filename)
                        EDVerbose.ERROR("I will now delete this file: %s and re-create it " % filename)
                        try:
                            os.remove(filename)
                        except Exception:
                            EDVerbose.ERROR("Fatal error !!! no way to recreate this corruped file %s" % filename)
                            raise
                        cls.__dictHDF5[filename] = h5py.File(filename)
            if not filename in cls.__dictLock:
                cls.__dictLock[filename] = Semaphore()
            filelock = cls.__dictLock[filename]
        with filelock:
            hdf5 = cls.__dictHDF5[filename]
            attrs = hdf5.attrs
            if "/" in dictAttributes:
                for key in dictAttributes["/"]:
                    if not key in attrs:
                        attrs.create(key, dictAttributes["/"][key])
            for key in cls.HDF5_ROOT_ATTRIBUTES:
                if not key in attrs.keys():
                    attrs.create(key, cls.HDF5_ROOT_ATTRIBUTES[key])
            if "file_name" not in attrs:
                file_name = os.path.basename(filename)
                if isinstance(file_name, unicode):
                    file_name = file_name.encode(cls.ENCODING)
                attrs.create("file_name", os.path.basename(file_name))
            if not "file_time" in attrs.keys():
                attrs.create("file_time", cls.getIsoTime())
            hdf5group = hdf5
            for subpath in h5path.split("/"):
                if subpath == "":
                    continue
                hdf5group = hdf5group.require_group(subpath)
                if hdf5group.name in dictAttributes:
                    for key in dictAttributes[hdf5group.name]:
                        if not key in hdf5group.attrs:
                            hdf5group.attrs.create(key, dictAttributes[hdf5group.name][key])
                for key in cls.HDF5_GROUP_ATTRIBUTES:
                    if key not in hdf5group.attrs:
                        hdf5group.attrs.create(key, cls.HDF5_GROUP_ATTRIBUTES[key])
            for key in cls.NX_GROUP_ATTRIBUTES:
                if key not in hdf5group.attrs:
                    hdf5group.attrs.create(key, cls.NX_GROUP_ATTRIBUTES[key])
        return hdf5group


    def flush(self, filename=None):
        """
        method to flush (optionaly another) hdf5 file
        """
        if filename:
            self.flushFile(filename)
        else:
            self.flushFile(self.strHDF5Filename)

    @classmethod
    def flushFile(cls, filename):
        """
        Write down to the disk the HDF5 file.
        
        @param filename: path of the file to be created
        @type filename: string
        """
        if filename in cls.__dictHDF5:
            EDVerbose.log("Flushing HDF5 buffer for " + filename)
            with cls.__dictLock[filename]:
                cls.__dictHDF5[filename].attrs.create("file_update_time", cls.getIsoTime())

                if h5py.version.api_version_tuple < (1, 10):
                    cls.__dictHDF5[filename].close()
                    cls.__dictHDF5[filename] = h5py.File(filename)
                else:
                    cls.__dictHDF5[filename].flush()
        else:
            EDVerbose.WARNING("HDF5 Flush: %s, no such file under control" % filename)



    @classmethod
    @deprecated
    def lockFile(cls, filename):
        """
        acquire the semaphore for this specific file
        """
        if filename in cls.__dictLock:
            cls.__dictLock[filename].acquire()
        else:
            EDVerbose.WARNING("EDPluginHDF5.lockFile: file not under supervision %s " % filename)

    @classmethod
    def releaseFile(cls, filename):
        """
        release the semaphore for this specific file
        """
        if filename in cls.__dictLock:
            cls.__dictLock[filename].release()
        else:
            EDVerbose.WARNING("EDPluginHDF5.releaseFile: file not under supervision %s " % filename)

    @classmethod
    def getFileLock(cls, filename):
        """
        return the semaphore for locking ....
        """
        if filename in cls.__dictLock:
            return cls.__dictLock[filename]
        else:
            EDVerbose.WARNING("EDPluginHDF5.getFileSem: file not under supervision %s. Expect failure ! " % filename)

    @classmethod
    def flushAll(cls):
        """
        Write down to the disk all HDF5 files under control.
        """
        with cls.__semCls:
            for filename in cls.__dictHDF5:
                cls.flushFile(filename)


    @classmethod
    def close(cls, filename):
        """
        Write down to the disk the HDF5 file and close it.
        
        @param filename: path of the file to be created
        @type filename: string
        """
        if cls.__dictHDF5.has_key(filename):
            with cls.__semCls:
                EDVerbose.log("Closing HDF5 file " + filename)
                with cls.__dictLock.pop(filename):
                    hdf5File = cls.__dictHDF5.pop(filename)
                    hdf5File.attrs.create("file_update_time", cls.getIsoTime())
                    hdf5File.close()
        else:
            EDVerbose.WARNING("HDF5 Flush: %s, no such file under control" % filename)


    @classmethod
    def closeAll(cls):
        """
        Write down to the disk all the HDF5 file and close them all.
        """
        with cls.__semCls:
            for filename in cls.__dictHDF5.copy():
                EDVerbose.log("Closing HDF5 file " + filename)
                with cls.__dictLock.pop(filename):
                    hdf5File = cls.__dictHDF5.pop(filename)
                    hdf5File.attrs.create("file_update_time", cls.getIsoTime())
                    hdf5File.close()


    @classmethod
    def getHDF5File(cls, filename):
        """
        Retieve a HDF5 file object from the cache
        
        @param filename: path of the file to be created
        @type filename: string
        """
        if filename in cls.__dictHDF5:
            return  cls.__dictHDF5[filename]
        else:
            EDVerbose.ERROR("EDPluginHDF5.getHDF5File: No such file: %s" % filename)


    @classmethod
    def getDataChunk(cls, filename, h5path, indexes=None):
        """
        Write down to the disk the HDF5 file and close it.
        
        @param filename: path of the file to be created
        @type filename: string
        @param h5path: path to the dataset of the internal NeXus structure to be read and returned
        @type  h5path: string
        @param indexes: limit indexes of the data chunk to retrieve from the file, the size of the list should be the same as the dimension of the data block 
        @type indexes: string representing the list of lists of integer like "[ [1,5], [3,4], [7,9] ]"  
        @return: the piece of data wanted  
        @rtype: numpy array
        """
        EDVerbose.WARNING("What about unicode and hdf5 bug ? please fixe this !")
        npArray = None
        if filename in cls.__dictHDF5:
            h5file = cls.__dictHDF5[filename]
            try:
                dataset = h5file[h5path]
            except Exception:
                EDVerbose.ERROR("HDF5 getDataChunk: %s, no such data structure in file %s" % (h5path, filename))
                raise
            if indexes is not None:
                try:
                    npArray = eval("dataset.value%s " % indexes)
                except NameError:
                    EDVerbose.ERROR("HDF5 getDataChunk: Malformed indexes for file %s, h5path %s, indexes %s. The dataset has this shape: " % (filename, h5path, indexes))
                    raise
                except ValueError:
                    EDVerbose.ERROR("HDF5 getDataChunk: Out of range indexes for file %s, h5path %s, indexes %s. The dataset has this shape: " % (filename, h5path, indexes))
                    raise
            else: #return the whole dataset
                npArray = dataset.value

        else:
            EDVerbose.ERROR("HDF5 getDataChunk: %s, no such file under control" % filename)
            raise
        return npArray


    @classmethod
    def getIsoTime(cls, forceTime=None):
        """
        @param forceTime: enforce a given time (current by default)
        @type forceTime: float
        @return: the current time as an ISO8601 string
        @rtype: string  
        """
        if forceTime is None:
            forceTime = time.time()
        localtime = time.localtime(forceTime)
        gmtime = time.gmtime(forceTime)
        tz_h = localtime.tm_hour - gmtime.tm_hour
        tz_m = localtime.tm_min - gmtime.tm_min
        return "%s%+03i:%02i" % (time.strftime("%Y-%m-%dT%H:%M:%S", localtime), tz_h, tz_m)


    def get_iChunkSegmentation(self):
        return self.__iChunkSegmentation
    iChunkSegmentation = property(get_iChunkSegmentation)

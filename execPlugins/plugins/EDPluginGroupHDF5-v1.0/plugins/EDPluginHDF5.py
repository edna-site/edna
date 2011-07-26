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

__author__ = "Jérôme Kieffer"
__contact__ = "jerome.kieffer@esrf.eu"
__license__ = "GPLv3+"
__copyright__ = "ESRF Grenoble"
__date__ = "2011/05/11"

###############################################################################
# BIG FAT WARNING
# HDF5 does not like unicode string and crashes with cryptic error messages
###############################################################################

import os, threading, time, locale
from EDVerbose                  import EDVerbose
from EDPluginExec               import EDPluginExec
from EDAssert                   import EDAssert
from EDUtilsPlatform            import EDUtilsPlatform
from EDConfiguration            import EDConfiguration
from EDFactoryPluginStatic      import EDFactoryPluginStatic
from XSDataHDF5v1_0             import XSDataInputHDF5Writer
architecture = EDUtilsPlatform.architecture
numpyPath = os.path.join(os.environ["EDNA_HOME"], "libraries", "20090405-Numpy-1.3", architecture)
h5pyPath = os.path.join(os.environ["EDNA_HOME"], "libraries", "H5Py-1.3.0", architecture)
fabioPath = os.path.join(os.environ["EDNA_HOME"], "libraries", "FabIO-0.0.7", architecture)
imagingPath = os.path.join(os.environ["EDNA_HOME"], "libraries", "20091115-PIL-1.1.7", architecture)

numpy = EDFactoryPluginStatic.preImport("numpy", numpyPath, _strMethodVersion="version.version")
h5py = EDFactoryPluginStatic.preImport("h5py", h5pyPath,)
fabio = EDFactoryPluginStatic.preImport("fabio", fabioPath)
Image = EDFactoryPluginStatic.preImport("Image", imagingPath)

if "EDNA_SITE" not in os.environ:
    os.environ["EDNA_SITE"] = "edna-site"


class EDPluginHDF5(EDPluginExec):
    """
    This is a common part for all EDNA plugin writing HDF5. most methods are class methods 
    """
    __semaphore = threading.Semaphore()
    __dictHDF5 = {} #key: filename, value: hdf5 h5py objects
    __dictLock = {} #key: filename, value:semaphores for writing
    HDF5_Multifiles = False
    HDF5_Compression = None
    CONF_COMPRESSION_KEY = "compression"
    ENCODING = max("ASCII", locale.getdefaultlocale()[1])
#    if ENCODING is None: ENCODING = "ASCII"
    HDF5_ROOT_ATTRIBUTES = {#"NeXus_version":"4.3.0",
                            "HDF5_Version":h5py.version.hdf5_version,
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
        EDPluginExec.__init__(self)
        self.strHDF5Filename = None
        self.strHDF5Path = None
        self.dtype = None
        self.dictExtraAttributes = {} #key= h5path, value dict of attributes
        self.__iChunkSegmentation = 1
        self.__startTime = time.time()


    def checkParameters(self):
        """
        Checks the mandatory parameters.
        """
        EDPluginExec.checkParameters(self)
        self.DEBUG("EDPluginHDF5.checkParameters")
        self.checkMandatoryParameters(self.getDataInput(), "Data Input is None")
        self.checkMandatoryParameters(self.getDataInput().getHDF5File(), "No HDF5 file provided")
        self.checkMandatoryParameters(self.getDataInput().getInternalHDF5Path(), "No HDF5 internal path provided")


    def configure(self):
        """
        Configure the HDF5 compression scheme
        """
        EDPluginExec.configure(self)
        self.DEBUG("EDPluginHDF5.configure")
        xsPluginItem = self.getConfiguration()
        if xsPluginItem is not None:
            strCompression = EDConfiguration.getStringParamValue(xsPluginItem, EDPluginHDF5.CONF_COMPRESSION_KEY)
            if strCompression != None:
                if strCompression == "None":
                    self.HDF5_Compression = None
                else:
                    self.HDF5_Compression = strCompression


    def preProcess(self, _edObject=None):
        EDPluginExec.preProcess(self)
        self.DEBUG("EDPluginHDF.preProcess")
        self.__startTime = time.time()
        self.strHDF5Filename = self.getDataInput().getHDF5File().getPath().getValue()
        self.strHDF5Path = self.getDataInput().getInternalHDF5Path().getValue()

        if self.getDataInput().multiFiles is not None:
            if self.getDataInput().multiFiles.value:
                base, ext = os.path.splitext(self.strHDF5Filename)
                self.strHDF5Filename = base + "%04d" + ext
                self.HDF5_Multifiles = True

        if self.getDataInput().forceDtype is not None:
            self.dtype = self.getDataInput().forceDtype.value
        for extraAttr in self.getDataInput().extraAttributes:
             attr = {}
             h5path = extraAttr.h5path.value
             for meta in extraAttr.metadata.keyValuePair:
                 attr[meta.key.value] = meta.value.value
             self.dictExtraAttributes[h5path] = attr
        if self.getDataInput().chunkSegmentation is not None:
            self._iChunkSegmentation = self.getDataInput().chunkSegmentation.value

    def postProcess(self, _edObject=None):
        self.DEBUG("EDPluginHDF5.postProcess")
        EDPluginExec.postProcess(self)
        if self.isVerboseDebug():
            self.flush(self.strHDF5Filename)
        self.log("EDPluginHDF5.postProcess %s: HDF5 writing took %.3fs" % (self.getId(), time.time() - self.__startTime))

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

        cls.__semaphore.acquire()
        if not cls.__dictHDF5.has_key(filename):

            if cls.HDF5_Multifiles:
                try:
                    cls.__dictHDF5[filename] = h5py.File(filename, driver="family")
                except:
                    EDVerbose.ERROR("Error in EDPluginHDF5.createStructure during opening HDF5 multi-file " + filename)
                    raise
            else:
                try:
                    cls.__dictHDF5[filename] = h5py.File(filename)
                except:
                    EDVerbose.ERROR("Error in EDPluginHDF5.createStructure during opening HDF5 file %s" % filename)
                    EDVerbose.ERROR("I will now delete this file: %s and re-create it " % filename)
                    try:
                        os.remove(filename)
                    except:
                        EDVerbose.ERROR("Fatal error !!! no way to recreate this corruped file %s" % filename)
                        raise
                    cls.__dictHDF5[filename] = h5py.File(filename)
        if not filename in cls.__dictLock:
            cls.__dictLock[filename] = threading.Semaphore()
        cls.__semaphore.release()
        cls.lockFile(filename)
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
        cls.releaseFile(filename)
        return hdf5group


    @classmethod
    def flush(cls, filename):
        """
        Write down to the disk the HDF5 file.
        
        @param filename: path of the file to be created
        @type filename: string
        """
        if cls.__dictHDF5.has_key(filename):
            EDVerbose.DEBUG("Flushing HDF5 buffer for " + filename)
            cls.lockFile(filename)
            cls.__dictHDF5[filename].attrs.create("file_update_time", cls.getIsoTime())
            cls.__dictHDF5[filename].flush()
            cls.releaseFile(filename)
        else:
            EDVerbose.WARNING("HDF5 Flush: %s, no such file under control" % filename)


    @classmethod
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
    def flushAll(cls):
        """
        Write down to the disk all HDF5 files under control.
        """
        cls.__semaphore.acquire()
        for filename in cls.__dictHDF5:
            EDVerbose.DEBUG("Flushing HDF5 buffer for " + filename)
            cls.lockFile(filename)
            cls.__dictHDF5[filename].attrs.create("file_update_time", cls.getIsoTime())
            cls.__dictHDF5[filename].flush()
            cls.releaseFile(filename)
        cls.__semaphore.release()


    @classmethod
    def close(cls, filename):
        """
        Write down to the disk the HDF5 file and close it.
        
        @param filename: path of the file to be created
        @type filename: string
        """
        if cls.__dictHDF5.has_key(filename):
            cls.__semaphore.acquire()
            EDVerbose.DEBUG("Closing HDF5 file " + filename)
            sem = cls.__dictLock.pop(filename)
            sem.acquire()
            hdf5File = cls.__dictHDF5.pop(filename)
            hdf5File.attrs.create("file_update_time", cls.getIsoTime())
            hdf5File.close()
            sem.release()
            cls.__semaphore.release()
        else:
            EDVerbose.WARNING("HDF5 Flush: %s, no such file under control" % filename)


    @classmethod
    def closeAll(cls):
        """
        Write down to the disk all the HDF5 file and close them all.
        """
        cls.__semaphore.acquire()
        for filename in cls.__dictHDF5.copy():
            EDVerbose.DEBUG("Closing HDF5 file " + filename)
            sem = cls.__dictLock.pop(filename)
            sem.acquire()
            hdf5File = cls.__dictHDF5.pop(filename)
            hdf5File.attrs.create("file_update_time", cls.getIsoTime())
            hdf5File.close()
            sem.release()
        cls.__semaphore.release()


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
            except:
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
        if not forceTime:
            forceTime = time.time()
        return time.strftime("%Y-%m-%d %H:%M:%S %Z", time.localtime(forceTime))

    def get_iChunkSegmentation(self):
        return self.__iChunkSegmentation
    iChunkSegmentation = property(get_iChunkSegmentation)

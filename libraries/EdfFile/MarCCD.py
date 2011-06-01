import sys
import struct
import string
import numpy

class MarCCD:
    def __init__(self, filename):
        if isinstance(filename, file):
            fd = filename
        else:
            #the b is needed for windows
            fd = open(filename, 'rb')
        order = fd.read(2)
        if order == "II":
            #intel, little endian
            fileOrder = "little"
        elif order == "MM":
            #motorola, high endian
            fileOrder = "low"
        else:
            raise IOError, "File is not a Mar CCD file, nor a TIFF file"
        if sys.byteorder != fileOrder:
            swap = True
        else:
            swap = False
        self.__header = MccdHeader(fd)
        info = {}
        info.update(self.__header.getFormat())
        info.update(self.__header.getGonio())
        info.update(self.__header.getDetector())
        info.update(self.__header.getFile())
        nbytes = info["nfast"]* info["nslow"] * info["depth"]
        depth  = info["depth"]
        fd.seek(4096)
        if depth == 1:
            data = numpy.fromstring(fd.read(nbytes), numpy.uint8)
        elif depth == 2:
            data = numpy.fromstring(fd.read(nbytes), numpy.uint16)
        elif depth == 4:
            data = numpy.fromstring(fd.read(nbytes), numpy.uint32)
        if swap:
            data = data.byteswap()
        data.shape = info["nfast"], info["nslow"]
        self.__data = data
        self.__info = info
        if not isinstance(filename, file):
            fd.close()

    def getData(self, *var, **kw):
        return self.__data

    def getInfo(self, *var, **kw):
        return self.__info

class MccdHeader:
    formatHead = ["nfast",
                  "nslow",
                  "depth"]
    
    gonioHead= [    "xtal_to_detector",
            "beam_x",
            "beam_y",
            "integration_time",
            "exposure_time",
            "readout_time",
            "nreads",
            "start_twotheta",
            "start_omega",
            "start_chi",
            "start_kappa",
            "start_phi",
            "start_delta",
            "start_gamma",
            "start_xtal_to_detector",
            "end_twotheta",
            "end_omega",
            "end_chi",
            "end_kappa",
            "end_phi",
            "end_delta",
            "end_gamma",
            "end_xtal_to_detector",
            "rotation_axis",
            "rotation_range",
            "detector_rotx",
            "detector_roty",
            "detector_rotz"
            ]

    detectorHead= [ "detector_type",
            "pixelsize_x", #nanometers
            "pixelsize_y"  #nanometers
            ]

    fileHead= [     ("filetitle", 128),
            ("filepath", 128),
            ("filename", 64),
            ("acquire_timestamp", 32),
            ("header_timestamp", 32),
            ("save_timestamp", 32),
            ("file_comments", 512)
            ]

    def __init__(self, fd):
        self.gonioValue= []
        self.detectorValue= []
        self.fileValue= []
        self.datasetValue= None
        self.__read(fd)
        self.__unpack()

    def __read(self, fp):
        fp.seek(1024)           #standard TIFF header
        self.raw= fp.read(3072) #Mar CCD Header

    def __unpack(self):
        self.__unpack_format()  #256 unsigned int
        self.__unpack_gonio()
        self.__unpack_detector()
        self.__unpack_file()
        self.__unpack_dataset()

    def __unpack_format(self):
        if 0:
            self.__format = struct.unpack("256I", self.raw[0:256*4])
        else:
            self.__format = numpy.fromstring(self.raw[0:256*4], numpy.uint32)

    def __unpack_gonio(self):
        idx= 640
        size= struct.calcsize("i")
        for nb in range(len(self.gonioHead)):
            self.gonioValue.append(struct.unpack("i", self.raw[idx+nb*size:idx+(nb+1)*size])[0])

    def __unpack_detector(self):
        idx= 768
        size= struct.calcsize("i")
        for nb in range(len(self.detectorHead)):
            self.detectorValue.append(struct.unpack("i", self.raw[idx+nb*size:idx+(nb+1)*size])[0])

    def __unpack_file(self):
        idx= 1024
        for (name, size) in self.fileHead:
            self.fileValue.append(self.raw[idx:idx+size].replace("\x00",""))
            idx= idx+size

    def __unpack_dataset(self):
        idx= 2048
        txt = self.raw[idx:idx+512].replace("\x00", "")
        if len(txt):
            self.datasetValue= txt
        else:   self.datasetValue= None

    def getFormat(self):
        format = {}
        #for i in range(19, 30):
        #    print i, "VALUE =", self.__format[i]
        format['nfast']  = self.__format[20] #n pixels in one line
        format['nslow']  = self.__format[21] #n lines in image
        format['depth']  = self.__format[22] #n bytes per pixel
        return format

    def getGonio(self):
        gonio= {}
        for (name, value) in zip(self.gonioHead, self.gonioValue):
            gonio[name]= value
        return gonio

    def getDetector(self):
        det= {}
        for (name, value) in zip(self.detectorHead, self.detectorValue):
            det[name]= value
        return det

    def getFile(self):
        ffile= {}
        for (head, value) in zip(self.fileHead, self.fileValue):
            ffile[head[0]]= value
        return ffile

    def getDataset(self):
        return self.datasetValue

if __name__ == "__main__":
    import os
    from PyMca import EdfFile
    #fd = open('Cu_ZnO_20289.mccd', 'rb')
    filename = sys.argv[1]
    mccd = MarCCD(filename)
    edfFile = filename+".edf"
    if os.path.exists(edfFile):
        os.remove(edfFile)
    edf = EdfFile.EdfFile(edfFile)
    edf.WriteImage(mccd.getInfo(),mccd.getData())
    edf = None

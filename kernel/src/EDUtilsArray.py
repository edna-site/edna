# -*- coding: utf8 -*-
#
#    Project: The EDNA Kernel
#             http://www.edna-site.org
#
#    File: "$Id: EDUtilsPath.py 1484 2010-05-05 07:08:21Z svensson $"
#
#    Copyright (C) 2008-2009 European Synchrotron Radiation Facility
#                            Grenoble, France
#
#    Principal authors: Jérôme Kieffer (jerome.kieffer@esrf.fr)
# 
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    and the GNU Lesser General Public License  along with this program.  
#    If not, see <http://www.gnu.org/licenses/>.
#
__authors__ = [ "Jérôme Kieffer" ]
__contact__ = "jerome.kieffer@esrf.fr"
__license__ = "LGPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"


import base64, hashlib, sys, struct, threading

from EDVerbose import EDVerbose
from EDObject import EDObject
from XSDataCommon import XSDataArray, XSDataString
from EDAssert import EDAssert

try:
    import numpy
    bHaveNumpy = True
    floatType = (float, numpy.floating)
except ImportError:
    bHaveNumpy = False
    floatType = float


class EDUtilsArray(object):
    """
    This is a static utility class for handling numpy like arrays in XML.
    
    """
    dTypeSize = {"int64": 8,
                 "uint64": 8,
                 "int32": 4,
                 "uint32": 4,
                 "int16": 2,
                 "uint16": 2,
                 "int8": 1,
                 "uint8": 1,
                 "float32": 4,
                 "float64": 8}

    dTypeFormat = {"int64": "q",
                 "uint64": "Q",
                 "int32": "l",
                 "uint32": "L",
                 "int16": "h",
                 "uint16": "H",
                 "int8": "b",
                 "uint8": "B",
                 "float32": "f",
                 "float64": "d"}
    semArrayToXSData = threading.Semaphore()
    semXsDataToArray = threading.Semaphore()


    @staticmethod
    def arrayToXSData(_array, _bIncludeMd5sum=True, _bForceNoNumpy=False):
        """
        convert a numpy array or a list of list into an XSDataArray object
        @param _array: numpy array or array-like list  
        @param _bIncludeMd5sum: should the md5sum be added to the XSDataArray instance. 
                                It is useful when sending object through the network
                                It is a problem for testing
        @param _bForceNoNumpy: enables tests without numpy 
        @type includeMd5sum: boolean
        @return: XSDataArray instance
        """
        EDUtilsArray.semArrayToXSData.acquire()
        xsdArray = XSDataArray()
        stringArray = ""
        shape = None
        dtype = None
        sizeDtype = None
        if bHaveNumpy is True and _bForceNoNumpy is False:
            EDVerbose.DEBUG("EDUtilsArray.arrayToXSData with numpy")
            # Enforce little Endianness
            if sys.byteorder == "big":
                _array.byteswap(True)
            stringArray = _array.tostring()
            shape = _array.shape
            dtype = str(_array.dtype)
            sizeDtype = len(numpy.zeros(1, dtype=_array.dtype).tostring())

        else:
            EDVerbose.DEBUG("EDUtilsArray.arrayToXSData without numpy")
            sizeDtype = 8 # We enforce either double (float64) or int64 
            shape = []
            subarray = _array
            while True:
                try:
                    l = len(subarray)
                except TypeError:
                    break
                shape.append(l)
                if l > 0:
                    subarray = subarray[0]
                else:
                    break

            if len(shape) == 1:
                if isinstance(_array[0], floatType):
                    dtype = "float64"
                    stringArray = struct.pack("<" + "d" * shape[0], *_array)
                else:
                    dtype = "int64"
                    stringArray = struct.pack("<" + "l" * shape[0], *_array)
            elif len(shape) == 2:
                if isinstance(_array[0][0], floatType):
                    dtype = "float64"
                    lineshape = "<" + "d" * shape[-1]
                else:
                    dtype = "int64"
                    lineshape = "<" + "q" * shape[-1]
                for subarray in _array:
                    stringArray += struct.pack(lineshape, *subarray)
            elif len(shape) == 3:
                if isinstance(_array[0][0][0], floatType):
                    dtype = "float64"
                    lineshape = "<" + "d" * shape[-1]
                else:
                    dtype = "int64"
                    lineshape = "<" + "q" * shape[-1]
                for subarray in _array:
                    for subsubarray in subarray:
                        stringArray += struct.pack(lineshape, *subsubarray)
            else:
                EDVerbose.WARNING("EDUtilsArray.arrayToXSDataArray: Array too large %s " % (shape))
        xsdArray.setData(base64.b64encode(stringArray))
        xsdArray.setCoding(XSDataString("base64"))
        xsdArray.setShape(list(shape))
        xsdArray.setDtype(dtype)
        size = 1
        for i in shape:
            size *= i
        xsdArray.setSize(size)
        EDAssert.equal(size * sizeDtype, len(stringArray), "string representing the array has the right size")
        if _bIncludeMd5sum is True:
            xsdArray.setMd5sum(XSDataString(hashlib.md5(stringArray).hexdigest()))
        EDUtilsArray.semArrayToXSData.release()
        return xsdArray


    @staticmethod
    def xsDataToArray(_xsdata, _bCheckMd5sum=True, _bForceNoNumpy=False):
        """
        convert a XSDataArray into either a numpy array or a list of list 
        @param _xsdata: XSDataArray instance  
        @param checkMd5sum: Check if the data are correct based on the checksum 
                                It is useful when sending object through the network
                                It is a problem for testing                               
        @type _bCheckMd5sum: boolean
        @param _bForceNoNumpy: enables tests without numpy 
        @type _bForceNoNumpy: boolean
        @return: numpy array or array-like list depending on what is available on the computer
        """
        EDUtilsArray.semXsDataToArray.acquire()
        shape = tuple(_xsdata.getShape())
        encData = _xsdata.getData()
        iSize = _xsdata.getSize()
        dtype = str(_xsdata.getDtype())

        if _xsdata.getCoding() is not None:
            strCoding = _xsdata.getCoding().getValue()
            if strCoding == "base64":
                decData = base64.b64decode(encData)
            elif strCoding == "base32":
                decData = base64.b32decode(encData)
            elif strCoding == "base16":
                decData = base64.b16decode(encData)
            else:
                EDVerbose.WARNING("Unable to recognize the encoding of the data !!! got %s, expected base64, base32 or base16, I assume it is base64 " % strCoding)
                decData = base64.b64decode(encData)
        else:
            EDVerbose.WARNING("No coding provided, I assume it is base64 ")
            strCoding = "base64"
            decData = base64.b64decode(encData)
        EDVerbose.DEBUG("Reading numpy array: len(EncData)= %s, len(decData)=%s, shape=%s, size=%s, dtype=%s, coding=%s" % (len(encData), len(decData), shape, _xsdata.getSize(), _xsdata.getDtype(), strCoding))
        EDAssert.equal(len(decData), EDUtilsArray.dTypeSize[dtype] * iSize, "decoded data has the expected size")

        if (_xsdata.getMd5sum() is not None) and (_bCheckMd5sum is True):
            EDAssert.equal(_xsdata.getMd5sum().getValue() , hashlib.md5(decData).hexdigest(), "md5sum is correct")

        if bHaveNumpy is True and _bForceNoNumpy is False:
            EDVerbose.DEBUG("EDUtilsArray.xsDataToArray with numpy")
            try:
                matIn = numpy.fromstring(decData, dtype=_xsdata.getDtype())
            except:
                matIn = numpy.fromstring(decData, dtype=numpy.dtype(str(_xsdata.getDtype())))
            arrayOut = matIn.reshape(shape)
            # Enforce little Endianness
            if sys.byteorder == "big":
                arrayOut.byteswap(True)

        else:
            EDVerbose.DEBUG("EDUtilsArray.xsDataToArray without numpy")
            arrayOut = []
            lineshape = "<" + EDUtilsArray.dTypeFormat[dtype] * shape[-1]
            if len(shape) == 1:
                arrayOut = list(struct.unpack(lineshape, decData))
            elif len(shape) == 2:
                linesize = shape[-1] * EDUtilsArray.dTypeSize[dtype]
                for i in xrange(shape[0]):
                    arrayOut.append(list(struct.unpack(lineshape, decData[i * linesize :(i + 1) * linesize ])))
            elif len(shape) == 3:
                linesize = shape[-1] * EDUtilsArray.dTypeSize[dtype]
                imgsize = shape[-2] * linesize
                for i in xrange(shape[0]):
                    subarray = []
                    for j in xrange(shape[1]):
                        subarray.append(list(struct.unpack(lineshape, decData[imgsize * i + j * linesize :imgsize * i + (j + 1) * linesize ])))
                    arrayOut.append(subarray)

        EDUtilsArray.semXsDataToArray.release()
        return arrayOut

#/*##########################################################################
# Copyright (C) 2004-2007 European Synchrotron Radiation Facility
#
# This file is part of the PyMCA X-ray Fluorescence Toolkit developed at
# the ESRF by the Beamline Instrumentation Software Support (BLISS) group.
#
# This toolkit is free software; you can redistribute it and/or modify it 
# under the terms of the GNU General Public License as published by the Free
# Software Foundation; either version 2 of the License, or (at your option) 
# any later version.
#
# PyMCA is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# PyMCA; if not, write to the Free Software Foundation, Inc., 59 Temple Place,
# Suite 330, Boston, MA 02111-1307, USA.
#
# PyMCA follows the dual licensing model of Trolltech's Qt and Riverbank's PyQt
# and cannot be used as a free plugin for a non-free program. 
#
# Please contact the ESRF industrial unit (industry@esrf.fr) if this license 
# is a problem to you.
#############################################################################*/
"""
    EdfFile.py
    Generic class for Edf files manipulation.    

    Interface:
    ===========================
    class EdfFile:          
        __init__(self,FileName)	
        GetNumImages(self)
        def GetData(self,Index, DataType="",Pos=None,Size=None):
        GetPixel(self,Index,Position)
        GetHeader(self,Index)
        GetStaticHeader(self,Index)
        WriteImage (self,Header,Data,Append=1,DataType="",WriteAsUnsigened=0,ByteOrder="")


    Edf format assumptions:
    ===========================
    The following details were assumed for this implementation:
    - Each Edf file contains a certain number of data blocks.
    - Each data block represents data stored in an one, two or three-dimensional array.
    - Each data block contains a header section, written in ASCII, and a data section of
      binary information.
    - The size of the header section in bytes is a multiple of 1024. The header is
      padded with spaces (0x20). If the header is not padded to a multiple of 1024,
      the file is recognized, but the output is always made in this format.
    - The header section starts by '{' and finishes by '}'. It is composed by several
      pairs 'keyword = value;'. The keywords are case insensitive, but the values are case
      sensitive. Each pair is put in a new line (they are separeted by 0x0A). In the
      end of each line, a semicolon (;) separes the pair of a comment, not interpreted.
      Exemple:
        {
        ; Exemple Header
        HeaderID = EH:000001:000000:000000    ; automatically generated
        ByteOrder = LowByteFirst              ; 
        DataType = FloatValue                 ; 4 bytes per pixel
        Size = 4000000                        ; size of data section
        Dim_1= 1000                           ; x coordinates
        Dim_2 = 1000                          ; y coordinates
        
        (padded with spaces to complete 1024 bytes)
        }
    - There are some fields in the header that are required for this implementation. If any of
      these is missing, or inconsistent, it will be generated an error:
        Size: Represents size of data block
        Dim_1: size of x coordinates (Dim_2 for 2-dimentional images, and also Dim_3 for 3d)
        DataType
        ByteOrder
    - For the written images, these fields are automatically genereted:
        Size,Dim_1 (Dim_2 and Dim_3, if necessary), Byte Order, DataType, HeaderID and Image
      These fields are called here "static header", and can be retrieved by the method
      GetStaticHeader. Other header components are taken by GetHeader. Both methods returns
      a dictionary in which the key is the keyword of the pair. When writting an image through
      WriteImage method, the Header parameter should not contain the static header information,
      which is automatically generated.
    - The indexing of images through these functions is based just on the 0-based position in
      the file, the header items HeaderID and Image are not considered for referencing the
      images.
    - The data section contais a number of bytes equal to the value of Size keyword. Data
      section is going to be translated into an 1D, 2D or 3D Numpy Array, and accessed
      through GetData method call.      
"""
__author__ =  'Alexandre Gobbo (gobbo@esrf.fr)'
__version__=  '$Revision: 1.21 $'

################################################################################  
import sys, string
import re
import numpy
import os.path , tempfile, shutil
import gzip

try:
    from FastEdf import extended_fread
    CAN_USE_FASTEDF = 1
except Exception:
    CAN_USE_FASTEDF = 0

################################################################################
# constants
HEADER_BLOCK_SIZE = 1024
STATIC_HEADER_ELEMENTS=("HeaderID","Image","ByteOrder","DataType",
                        "Dim_1","Dim_2","Dim_3",
                        "Offset_1","Offset_2","Offset_3",
                        "Size")
STATIC_HEADER_ELEMENTS_CAPS=("HEADERID","IMAGE","BYTEORDER","DATATYPE",
                             "DIM_1","DIM_2","DIM_3",
                             "OFFSET_1","OFFSET_2","OFFSET_3",
                             "SIZE")

LOWER_CASE=0
UPPER_CASE=1

KEYS=1
VALUES=2

###############################################################################
class Image:
    """
    """
    def __init__(self):
        """ Constructor
        """
        self.Header={}
        self.StaticHeader={}
        self.HeaderPosition=0
        self.DataPosition=0
        self.Size=0
        self.NumDim=1
        self.Dim1=0
        self.Dim2=0
        self.Dim3=0
        self.DataType=""
        #for i in STATIC_HEADER_ELEMENTS: self.StaticHeader[i]=""
   
################################################################################

class  EdfFile:    
    """
    """
    ############################################################################
    #Interface
    def __init__(self,FileNameOrFileDescriptor,fastedf=None):
        """ Constructor
            FileNameOrFileDescriptor:   Name of the file (either existing or to be created) or file descriptor
        """
        self.Images=[]
        self.NumImages=0

        if isinstance(FileNameOrFileDescriptor,str) or isinstance(FileNameOrFileDescriptor,unicode):
            self.File = None
            self.FileName = FileNameOrFileDescriptor
        else:
            self.File = FileNameOrFileDescriptor
            try:
                self.FileName = FileNameOrFileDescriptor.name
            except AttributeError:
                self.FileName = FileNameOrFileDescriptor.filename
            
        if fastedf is None:fastedf=0
        self.fastedf=fastedf
        
        if sys.byteorder=="big": self.SysByteOrder="HighByteFirst"
        else: self.SysByteOrder="LowByteFirst"

        if self.File is None:
            self.__ownedOpen = True
            try:
                if os.path.isfile(self.FileName)==0:                
                    self.File = open(self.FileName, "wb")
                    self.File.close()    

                if (os.access(self.FileName,os.W_OK)):
                    self.File=open(self.FileName, "r+b")
                else : 
                    self.File=open(self.FileName, "rb")

                self.File.seek(0, 0)
            except Exception:
                try:
                    self.File.close()
                except Exception:
                    pass
                raise "EdfFile: Error opening file"
        else: self.__ownedOpen = False

        Index=0

        self.__checkEdfFile = re.compile('^dim_1',re.IGNORECASE|re.MULTILINE)

        self.File.seek(0, 0)
	if self.File.read(1) == '':
	    return 
        self.File.seek(0, 0)

        startHeaderPos = self.File.tell()
        header,headersize = self.__readOneHeader()
        while 1 :
            img = Image()
            img.HeaderPosition = startHeaderPos
            img.DataPosition = startHeaderPos + headersize
            StaticHeader = {}
            for line in header.split('\n') :
                posSemiColumn = line.rfind(';')
                if posSemiColumn < 0: continue
                else:
                    line = line[:posSemiColumn]
                try:
                    key,value = line.split('=')
                    key = key.strip()
                    value = value.strip()
                except ValueError: continue
                keyCap = key.upper()
                if keyCap in STATIC_HEADER_ELEMENTS_CAPS :
                    img.StaticHeader[key] = value
                    StaticHeader[keyCap] = value
                else:
                    img.Header[key] = value
            #Check Image Size
            try:
                stringSize = StaticHeader['SIZE']
                imageSize = int(stringSize)
                img.Size = imageSize
                self.File.seek(img.DataPosition + imageSize)
                startHeaderPos = self.File.tell()
            except KeyError:
                raise "EdfFile: Image doesn't have size information"
            except ValueError:
                raise "EdfFile: Image size information is not an integer"
            #Check DataType
            try:
                img.DataType = StaticHeader["DATATYPE"]
            except KeyError:
                raise "EdfFile: Image doesn't have datatype information"
            #Check ByteOrder
            try:
                img.ByteOrder = StaticHeader["BYTEORDER"]
            except KeyError:
                raise "EdfFile: Image doesn't have byteorder information"
            #Check DIM1
            try:
                stringDim1 = StaticHeader["DIM_1"]
                img.Dim1 = int(stringDim1)
                try:
                    img.Offset1 = int(StaticHeader.get('OFFSET_1','0'))
                except ValueError:
                    img.Offset1 = 0
            except KeyError:
                raise "EdfFile: Image doesn't have dimension information"
            #DIM2
            stringDim2 = StaticHeader.get("DIM_2",None)
            if stringDim2 is not None:
                img.Dim2 = int(stringDim2)
                try:
                    img.Offset2 = int(StaticHeader.get("OFFSET_2","0"))
                except ValueError:
                    img.Offset2 = 0
                img.NumDim = 2
            #DIM3
            stringDim3 = StaticHeader.get("DIM_3",None)
            if stringDim3 is not None:
                img.Dim3 = int(stringDim3)
                try:
                    img.Offset3 = int(StaticHeader.get("OFFSET_3","0"))
                except ValueError:
                    img.Offset3 = 0
                img.NumDim = 3
            #APPEND IMAGE
            self.Images.append(img)
            self.NumImages += 1
            try:
                header,headersize = self.__readOneHeader()
            except Exception: break
        
    def GetNumImages(self):
        """ Returns number of images of the object (and associated file)
        """
        return self.NumImages

        
    
    def GetData(self,Index, DataType="",Pos=None,Size=None):
        """ Returns numpy array with image data
            Index:          The zero-based index of the image in the file
            DataType:       The edf type of the array to be returnd
                            If ommited, it is used the default one for the type
                            indicated in the image header
                            Attention to the absence of UnsignedShort,
                            UnsignedInteger and UnsignedLong types in
                            Numpy Python
                            Default relation between Edf types and NumPy's typecodes:
                                SignedByte          int8   b
                                UnsignedByte        uint8  B       
                                SignedShort         int16  h
                                UnsignedShort       uint16 H
                                SignedInteger       int32  i
                                UnsignedInteger     uint32 I
                                SignedLong          int32  i
                                UnsignedLong        uint32 I
                                Signed64            int64  (l in 64bit, q in 32 bit)
                                Unsigned64          uint64 (L in 64bit, Q in 32 bit) 
                                FloatValue          float32 f
                                DoubleValue         float64 d
            Pos:            Tuple (x) or (x,y) or (x,y,z) that indicates the begining
                            of data to be read. If ommited, set to the origin (0),
                            (0,0) or (0,0,0)
            Size:           Tuple, size of the data to be returned as x) or (x,y) or
                            (x,y,z) if ommited, is the distance from Pos to the end.

            If Pos and Size not mentioned, returns the whole data.                         
        """
        fastedf = self.fastedf
        if Index < 0 or Index >= self.NumImages: raise ValueError, "EdfFile: Index out of limit"
        if fastedf is None:fastedf = 0
        if Pos is None and Size is None:
            self.File.seek(self.Images[Index].DataPosition,0)
            datatype = self.__GetDefaultNumpyType__(self.Images[Index].DataType, index= Index)
            try:
                datasize = self.__GetSizeNumpyType__(datatype)
            except TypeError:
                print "What is the meaning of this error?"
                datasize = 8
            if self.Images[Index].NumDim==3:
                sizeToRead = self.Images[Index].Dim1 * \
                             self.Images[Index].Dim2 * \
                             self.Images[Index].Dim3 * datasize
                Data = numpy.fromstring(self.File.read(sizeToRead),
                            datatype)
                Data = numpy.reshape(Data, (self.Images[Index].Dim3,self.Images[Index].Dim2, self.Images[Index].Dim1))
            elif self.Images[Index].NumDim==2:
                sizeToRead = self.Images[Index].Dim1 * \
                             self.Images[Index].Dim2 * datasize
                Data = numpy.fromstring(self.File.read(sizeToRead),
                            datatype)
                #print "datatype = ",datatype
                #print "Data.type = ", Data.dtype.char
                #print "self.Images[Index].DataType ", self.Images[Index].DataType
                #print "Data.shape",Data.shape
                #print "datasize = ",datasize
                #print "sizeToRead ",sizeToRead 
                #print "lenData = ", len(Data)
                Data = numpy.reshape(Data, (self.Images[Index].Dim2, self.Images[Index].Dim1))
            elif self.Images[Index].NumDim==1:
                sizeToRead = self.Images[Index].Dim1 * datasize
                Data = numpy.fromstring(self.File.read(sizeToRead),
                            datatype)
        elif fastedf and CAN_USE_FASTEDF:
            type= self.__GetDefaultNumpyType__(self.Images[Index].DataType, index= Index)
            size_pixel=self.__GetSizeNumpyType__(type)
            Data=Numpy.array([],type)
            if self.Images[Index].NumDim==1:
                if Pos==None: Pos=(0,)
                if Size==None: Size=(0,)
                sizex=self.Images[Index].Dim1
                Size=list(Size)                
                if Size[0]==0:Size[0]=sizex-Pos[0]
                self.File.seek((Pos[0]*size_pixel)+self.Images[Index].DataPosition,0)
                Data = numpy.fromstring(self.File.read(Size[0]*size_pixel), type)
            elif self.Images[Index].NumDim==2:                
                if Pos==None: Pos=(0,0)
                if Size==None: Size=(0,0)
                Size=list(Size)
                sizex,sizey=self.Images[Index].Dim1,self.Images[Index].Dim2
                if Size[0]==0:Size[0]=sizex-Pos[0]
                if Size[1]==0:Size[1]=sizey-Pos[1]
                Data=numpy.zeros([Size[1],Size[0]],type)
                self.File.seek((((Pos[1]*sizex)+Pos[0])*size_pixel)+self.Images[Index].DataPosition,0)
                extended_fread(Data, Size[0]*size_pixel , numpy.array([Size[1]]),
                               numpy.array([sizex*size_pixel]) ,self.File)

            elif self.Images[Index].NumDim==3:
                if Pos==None: Pos=(0,0,0)
                if Size==None: Size=(0,0,0)
                Size=list(Size)
                sizex,sizey,sizez=self.Images[Index].Dim1,self.Images[Index].Dim2,self.Images[Index].Dim3
                if Size[0]==0:Size[0]=sizex-Pos[0]
                if Size[1]==0:Size[1]=sizey-Pos[1]
                if Size[2]==0:Size[2]=sizez-Pos[2]
                Data=numpy.zeros([Size[2],Size[1],Size[0]],type)
                self.File.seek(((((Pos[2]*sizey+Pos[1])*sizex)+Pos[0])*size_pixel)+self.Images[Index].DataPosition,0)
                extended_fread(Data, Size[0]*size_pixel , numpy.array([Size[2],Size[1]]),
                        numpy.array([ sizey*sizex*size_pixel , sizex*size_pixel]) ,self.File)

        else:
            if fastedf:print "I could not use fast routines"
            type= self.__GetDefaultNumpyType__(self.Images[Index].DataType, index= Index)
            size_pixel=self.__GetSizeNumpyType__(type)
            Data=numpy.array([],type)
            if self.Images[Index].NumDim==1:
                if Pos==None: Pos=(0,)
                if Size==None: Size=(0,)
                sizex=self.Images[Index].Dim1
                Size=list(Size)                
                if Size[0]==0:Size[0]=sizex-Pos[0]
                self.File.seek((Pos[0]*size_pixel)+self.Images[Index].DataPosition,0)
                Data = numpy.fromstring(self.File.read(Size[0]*size_pixel), type)
            elif self.Images[Index].NumDim==2:                
                if Pos==None: Pos=(0,0)
                if Size==None: Size=(0,0)
                Size=list(Size)
                sizex,sizey=self.Images[Index].Dim1,self.Images[Index].Dim2
                if Size[0]==0:Size[0]=sizex-Pos[0]
                if Size[1]==0:Size[1]=sizey-Pos[1]
                #print len(range(Pos[1],Pos[1]+Size[1])), "LECTURES OF ", Size[0], "POINTS"
                #print "sizex = ", sizex, "sizey = ", sizey
                Data = numpy.zeros((Size[1],Size[0]), type)
                dataindex =0
                for y in range(Pos[1],Pos[1]+Size[1]):
                    self.File.seek((((y*sizex)+Pos[0])*size_pixel)+self.Images[Index].DataPosition,0)
                    line = numpy.fromstring(self.File.read(Size[0]*size_pixel), type)
                    Data[dataindex,:] =  line[:]
                    #Data=numpy.concatenate((Data,line))
                    dataindex += 1
                #print "DataSize = ",Data.shape
                #print "Requested reshape = ",Size[1],'x',Size[0]
                #Data = numpy.reshape(Data, (Size[1],Size[0]))                            
            elif self.Images[Index].NumDim==3:
                if Pos==None: Pos=(0,0,0)
                if Size==None: Size=(0,0,0)
                Size=list(Size)
                sizex,sizey,sizez=self.Images[Index].Dim1,self.Images[Index].Dim2,self.Images[Index].Dim3
                if Size[0]==0:Size[0]=sizex-Pos[0]
                if Size[1]==0:Size[1]=sizey-Pos[1]
                if Size[2]==0:Size[2]=sizez-Pos[2]
                for z in range(Pos[2],Pos[2]+Size[2]):
                    for y in range(Pos[1],Pos[1]+Size[1]):
                        self.File.seek(((((z*sizey+y)*sizex)+Pos[0])*size_pixel)+self.Images[Index].DataPosition,0)
                        line = numpy.fromstring(self.File.read(Size[0]*size_pixel), type)
                        Data=numpy.concatenate((Data,line))                
                Data = numpy.reshape(Data, (Size[2],Size[1],Size[0]))

        if string.upper(self.SysByteOrder)!=string.upper(self.Images[Index].ByteOrder):
            Data=Data.byteswap()
        if DataType != "":
            Data=self.__SetDataType__ (Data,DataType)
        return Data



    def GetPixel(self,Index, Position):
        """ Returns double value of the pixel, regardless the format of the array
            Index:      The zero-based index of the image in the file
            Position:   Tuple with the coordinete (x), (x,y) or (x,y,z)
        """
        if Index < 0 or Index >= self.NumImages: raise ValueError, "EdfFile: Index out of limit"
        if len(Position)!= self.Images[Index].NumDim: raise ValueError, "EdfFile: coordinate with wrong dimension "
        
        size_pixel=self.__GetSizeNumpyType__(self.__GetDefaultNumpyType__(self.Images[Index].DataType), index= Index)
        offset=Position[0]*size_pixel
        if self.Images[Index].NumDim>1:
            size_row=size_pixel * self.Images[Index].Dim1
            offset=offset+ (Position[1]* size_row)
            if self.Images[Index].NumDim==3:
                size_img=size_row * self.Images[Index].Dim2
                offset=offset+ (Position[2]* size_img)
        self.File.seek(self.Images[Index].DataPosition + offset,0)
        Data = Numpy.fromstring(self.File.read(size_pixel), self.__GetDefaultNumpyType__(self.Images[Index].DataType, index= Index))
        if string.upper(self.SysByteOrder)!=string.upper(self.Images[Index].ByteOrder):
            Data=Data.byteswap() 
        Data=self.__SetDataType__ (Data,"DoubleValue")
        return Data[0]
         
        
    def GetHeader(self,Index):
        """ Returns dictionary with image header fields.
            Does not include the basic fields (static) defined by data shape, 
            type and file position. These are get with GetStaticHeader
            method.
            Index:          The zero-based index of the image in the file
        """
        if Index < 0 or Index >= self.NumImages: raise ValueError, "Index out of limit"
        #return self.Images[Index].Header
        ret={}
        for i in self.Images[Index].Header.keys():
            ret[i]=self.Images[Index].Header[i]        
        return ret

        
    def GetStaticHeader(self,Index):
        """ Returns dictionary with static parameters
            Data format and file position dependent information
            (dim1,dim2,size,datatype,byteorder,headerId,Image)
            Index:          The zero-based index of the image in the file
        """ 
        if Index < 0 or Index >= self.NumImages: raise ValueError, "Index out of limit"
        #return self.Images[Index].StaticHeader
        ret={}
        for i in self.Images[Index].StaticHeader.keys():
            ret[i]=self.Images[Index].StaticHeader[i]        
        return ret


    def WriteImage (self,Header,Data,Append=1,DataType="",ByteOrder=""):
        """ Writes image to the file. 
            Header:         Dictionary containing the non-static header
                            information (static information is generated
                            according to position of image and data format
            Append:         If equals to 0, overwrites the file. Otherwise, appends
                            to the end of the file
            DataType:       The data type to be saved to the file:
                                SignedByte          
                                UnsignedByte               
                                SignedShort         
                                UnsignedShort       
                                SignedInteger       
                                UnsignedInteger     
                                SignedLong          
                                UnsignedLong        
                                FloatValue          
                                DoubleValue         
                            Default: according to Data array typecode:
                                    1:  SignedByte
                                    b:  UnsignedByte
                                    s:  SignedShort       
				    w:  UnsignedShort
                                    i:  SignedInteger
                                    l:  SignedLong          
				    u:  UnsignedLong
                                    f:  FloatValue       
                                    d:  DoubleValue
            ByteOrder:      Byte order of the data in file:
                                HighByteFirst
                                LowByteFirst
                            Default: system's byte order
        """
        if Append==0:
            self.File.truncate(0)
            self.Images=[]
            self.NumImages=0
        Index=self.NumImages
        self.NumImages = self.NumImages + 1                
        self.Images.append(Image())

        #self.Images[Index].StaticHeader["Dim_1"] = "%d" % Data.shape[1]
        #self.Images[Index].StaticHeader["Dim_2"] = "%d" % Data.shape[0]
        if len(Data.shape)==1:
            self.Images[Index].Dim1=Data.shape[0]
            self.Images[Index].StaticHeader["Dim_1"] = "%d" % self.Images[Index].Dim1
            self.Images[Index].Size=(Data.shape[0]*\
                                     self.__GetSizeNumpyType__(Data.dtype))
        elif len(Data.shape)==2:
            self.Images[Index].Dim1=Data.shape[1]
            self.Images[Index].Dim2=Data.shape[0]
            self.Images[Index].StaticHeader["Dim_1"] = "%d" % self.Images[Index].Dim1
            self.Images[Index].StaticHeader["Dim_2"] = "%d" % self.Images[Index].Dim2
            self.Images[Index].Size=(Data.shape[0]*Data.shape[1]*\
                                     self.__GetSizeNumpyType__(Data.dtype))
            self.Images[Index].NumDim=2
        elif len(Data.shape)==3:
            self.Images[Index].Dim1=Data.shape[2]
            self.Images[Index].Dim2=Data.shape[1]
            self.Images[Index].Dim3=Data.shape[0]
            self.Images[Index].StaticHeader["Dim_1"] = "%d" % self.Images[Index].Dim1
            self.Images[Index].StaticHeader["Dim_2"] = "%d" % self.Images[Index].Dim2
            self.Images[Index].StaticHeader["Dim_3"] = "%d" % self.Images[Index].Dim3
            self.Images[Index].Size=(Data.shape[0]*Data.shape[1]*Data.shape[2]*\
                                     self.__GetSizeNumpyType__(Data.dtype))
            self.Images[Index].NumDim=3
        elif len(Data.shape)>3:
            raise TypeError, "EdfFile: Data dimension not suported"
        

        if DataType=="":
            self.Images[Index].DataType=self.__GetDefaultEdfType__(Data.dtype)
        else:
            self.Images[Index].DataType=DataType
            Data=self.__SetDataType__ (Data,DataType)
                            
        if ByteOrder=="":
            self.Images[Index].ByteOrder=self.SysByteOrder
        else:
            self.Images[Index].ByteOrder=ByteOrder
                
        self.Images[Index].StaticHeader["Size"]  = "%d" % self.Images[Index].Size
        self.Images[Index].StaticHeader["Image"] = Index+1
        self.Images[Index].StaticHeader["HeaderID"] = "EH:%06d:000000:000000" % self.Images[Index].StaticHeader["Image"]
        self.Images[Index].StaticHeader["ByteOrder"]=self.Images[Index].ByteOrder
        self.Images[Index].StaticHeader["DataType"]=self.Images[Index].DataType

        
        self.Images[Index].Header={}            
        self.File.seek(0,2)
        StrHeader = "{\n"
        for i in STATIC_HEADER_ELEMENTS:
            if i in self.Images[Index].StaticHeader.keys():
                StrHeader = StrHeader + ("%s = %s ;\n" % (i , self.Images[Index].StaticHeader[i]))
        for i in Header.keys():
            StrHeader = StrHeader + ("%s = %s ;\n" % (i,Header[i]))
            self.Images[Index].Header[i]=Header[i]
        newsize=(((len(StrHeader)+1)/HEADER_BLOCK_SIZE)+1)*HEADER_BLOCK_SIZE -2                   
        StrHeader = string.ljust(StrHeader,newsize)
        StrHeader = StrHeader+"}\n"

        self.Images[Index].HeaderPosition=self.File.tell()    
        self.File.write(StrHeader)
        self.Images[Index].DataPosition=self.File.tell()

        #if self.Images[Index].StaticHeader["ByteOrder"] != self.SysByteOrder:
        if string.upper(self.Images[Index].ByteOrder) != string.upper(self.SysByteOrder):
            self.File.write((Data.byteswap()).tostring())  
        else:
            self.File.write(Data.tostring())
        
        

    ############################################################################
    #Internal Methods
        
    def __GetDefaultNumpyType__(self, EdfType, index=None):
        """ Internal method: returns NumPy type according to Edf type
        """
        return self.GetDefaultNumpyType(EdfType, index)

    def __GetDefaultEdfType__(self, NumpyType):
        """ Internal method: returns Edf type according Numpy type
        """
        if   NumpyType in ["b",   numpy.int8]:            return "SignedByte"
        elif NumpyType in ["B",  numpy.uint8]:            return "UnsignedByte"
        elif NumpyType in ["h",  numpy.int16]:            return "SignedShort"          
        elif NumpyType in ["H", numpy.uint16]:            return "UnsignedShort"          
        elif NumpyType in ["i",  numpy.int32]:            return "SignedInteger"  
        elif NumpyType in ["I", numpy.uint32]:            return "UnsignedInteger"  
        elif NumpyType == "l":
            if sys.platform == 'linux2':
                return "Signed64"           
            else:
                return "SignedLong"           
        elif NumpyType == "L":
            if sys.platform == 'linux2':
                return "Unsigned64"           
            else:
                return "UnsignedLong"
        elif NumpyType == numpy.int64:                     return "Signed64"
        elif NumpyType == numpy.uint64:                    return "Unsigned64"
        elif NumpyType in ["f", numpy.float32]:            return "FloatValue"         
        elif NumpyType in ["d", numpy.float64]:            return "DoubleValue"
        else: raise TypeError, "unknown NumpyType %s" % NumpyType


    def __GetSizeNumpyType__(self, NumpyType):
        """ Internal method: returns size of NumPy's Array Types
        """
        if   NumpyType in ["b",   numpy.int8]:  return 1
        elif NumpyType in ["B",  numpy.uint8]:  return 1
        elif NumpyType in ["h",  numpy.int16]:  return 2          
        elif NumpyType in ["H", numpy.uint16]:  return 2          
        elif NumpyType in ["i",  numpy.int32]:  return 4  
        elif NumpyType in ["I", numpy.uint32]:  return 4  
        elif NumpyType == "l":            
            if sys.platform == 'linux2':
                return 8    #64 bit
            else:
                return 4    #32 bit
        elif NumpyType == "L":
            if sys.platform == 'linux2':
                return 8    #64 bit
            else:
                return 4    #32 bit
        elif NumpyType in ["f", numpy.float32]: return 4         
        elif NumpyType in ["d", numpy.float64]: return 8
        elif NumpyType == "Q":            return 8 #unsigned 64 in 32 bit
        elif NumpyType == "q":            return 8 #signed 64 in 32 bit
        elif NumpyType == numpy.uint64:   return 8
        elif NumpyType == numpy.int64:    return 8
        else: raise TypeError, "unknown NumpyType %s" % NumpyType


    def __SetDataType__ (self, Array, DataType):
        """ Internal method: array type convertion
        """
        # AVOID problems not using FromEdfType= Array.dtype.char
        FromEdfType= Array.dtype
        ToEdfType= self.__GetDefaultNumpyType__(DataType)
        if ToEdfType != FromEdfType:
            aux=Array.astype(self.__GetDefaultNumpyType__(DataType))    
            return aux
        return Array

    def __del__(self):
        try:
            if self.__ownedOpen:
                self.File.close()
        except Exception:
            pass

    def GetDefaultNumpyType(self, EdfType, index=None):
        """ Returns NumPy type according Edf type
        """
        if index is None:return GetDefaultNumpyType(EdfType)
        EdfType=string.upper(EdfType)
        if EdfType in ['SIGNED64']  :return numpy.int64
        if EdfType in ['UNSIGNED64']:return numpy.uint64
        if EdfType in ["SIGNEDLONG", "UNSIGNEDLONG"]:
            dim1 = 1
            dim2 = 1
            dim3 = 1 
            if hasattr(self.Images[index],"Dim1"):
                dim1 = self.Images[index].Dim1
                if hasattr(self.Images[index],"Dim2"):
                    dim2 = self.Images[index].Dim2
                    if dim2 <= 0: dim2 = 1
                    if hasattr(self.Images[index],"Dim3"):
                        dim3 = self.Images[index].Dim3
                        if dim3 <= 0: dim3 = 1
                if hasattr(self.Images[index],"Size"):
                    size = self.Images[index].Size
                    if size/(dim1*dim2*dim3) == 8:
                        if EdfType == "UNSIGNEDLONG":
                            return numpy.uint64
                        else:
                            return numpy.int64
            if EdfType == "UNSIGNEDLONG":
                return numpy.uint32
            else:
                return numpy.int32
            
        return GetDefaultNumpyType(EdfType)
        
    def __readOneHeader(self) :
        buffer = self.File.read(512)
        #TEST if it's an EDF File
        if not self.__checkEdfFile.search(buffer) :
            raise IOError, "EdfFile : not an Edf format"
        startFind = 0
        while 1:
            endHeader = -1
            while 1:
                endTmp = buffer.rfind('}',startFind,endHeader)
                if endTmp > -1:
                    endHeader = endTmp
                else: break
            if endHeader > -1 : break
            buffer += self.File.read(512)
            startFind += 512
        lastnewline = buffer.find('\n',endHeader)
        if endHeader < lastnewline <= endHeader + 2:
            endHeader = lastnewline
        return (buffer,endHeader + 1)

def GetDefaultNumpyType(EdfType):
    """ Returns NumPy type according Edf type
    """
    EdfType=string.upper(EdfType)
    if   EdfType == "SIGNEDBYTE":       return numpy.int8   # "b"
    elif EdfType == "UNSIGNEDBYTE":     return numpy.uint8  # "B"       
    elif EdfType == "SIGNEDSHORT":      return numpy.int16  # "h"
    elif EdfType == "UNSIGNEDSHORT":    return numpy.uint16 # "H"
    elif EdfType == "SIGNEDINTEGER":    return numpy.int32  # "i"
    elif EdfType == "UNSIGNEDINTEGER":  return numpy.uint32 # "I"
    elif EdfType == "SIGNEDLONG":       return numpy.int32  # "i" #ESRF acquisition is made in 32bit
    elif EdfType == "UNSIGNEDLONG":     return numpy.uint32 # "I" #ESRF acquisition is made in 32bit
    elif EdfType == "SIGNED64":         return numpy.int64  # "l"
    elif EdfType == "UNSIGNED64":       return numpy.uint64 # "L"
    elif EdfType == "FLOATVALUE":       return numpy.float32 # "f"
    elif EdfType == "FLOAT":            return numpy.float32 # "f"
    elif EdfType == "DOUBLEVALUE":      return numpy.float64 # "d"
    else: raise TypeError, "unknown EdfType %s" % EdfType


def SetDictCase(Dict, Case, Flag):
    """ Returns dictionary with keys and/or values converted into upper or lowercase
        Dict:   input dictionary
        Case:   LOWER_CASE, UPPER_CASE
        Flag:   KEYS, VALUES or KEYS | VALUES        
    """
    newdict={}
    for i in Dict.keys():
        newkey=i
        newvalue=Dict[i]
        if Flag & KEYS:
            if Case == LOWER_CASE:  newkey = string.lower(newkey)
            else:                   newkey = string.upper(newkey)
        if Flag & VALUES:
            if Case == LOWER_CASE:  newvalue = string.lower(newvalue)
            else:                   newvalue = string.upper(newvalue)
        newdict[newkey]=newvalue
    return newdict    


def GetRegion(Arr,Pos,Size):
    """Returns array with refion of Arr.
       Arr must be 1d, 2d or 3d
       Pos and Size are tuples in the format (x) or (x,y) or (x,y,z)
       Both parameters must have the same size as the dimention of Arr
    """
    Dim=len(Arr.shape)
    if len(Pos) != Dim:  return None
    if len(Size) != Dim: return None
    
    if (Dim==1):
        SizeX=Size[0]
        if SizeX==0: SizeX=Arr.shape[0]-Pos[0]
        ArrRet=numpy.take(Arr, range(Pos[0],Pos[0]+SizeX))
    elif (Dim==2):
        SizeX=Size[0]
        SizeY=Size[1]
        if SizeX==0: SizeX=Arr.shape[1]-Pos[0]
        if SizeY==0: SizeY=Arr.shape[0]-Pos[1]
        ArrRet=numpy.take(Arr, range(Pos[1],Pos[1]+SizeY))
        ArrRet=numpy.take(ArrRet, range(Pos[0],Pos[0]+SizeX),1)
    elif (Dim==3):
        SizeX=Size[0]
        SizeY=Size[1]
        SizeZ=Size[2]
        if SizeX==0: SizeX=Arr.shape[2]-Pos[0]
        if SizeY==0: SizeX=Arr.shape[1]-Pos[1]
        if SizeZ==0: SizeZ=Arr.shape[0]-Pos[2]
        ArrRet=numpy.take(Arr, range(Pos[2],Pos[2]+SizeZ))
        ArrRet=numpy.take(ArrRet, range(Pos[1],Pos[1]+SizeY),1)
        ArrRet=numpy.take(ArrRet, range(Pos[0],Pos[0]+SizeX),2)
    else:
        ArrRet=None
    return ArrRet

##@brief Edf class to read Gzip file
class EdfGzipFile(EdfFile) :
    def __init__(self,filename,**keys) :
        self.__gzipFd = EdfGzipFile._gzFile(filename)
        EdfFile.__init__(self,self.__gzipFd,**keys)

    class _gzFile(gzip.GzipFile) :
         def __init__(self,filepath,*args) :
                gzip.GzipFile.__init__(self,filepath,*args)
                self.name = filepath
                
         def seek(self,offset,whence = 0) :
                if whence == 0:
                    gzip.GzipFile.seek(self,offset)
                elif whence == 1:
                    pos = self.tell()
                    gzip.GzipFile.seek(self,pos + offset)
                else:
                    raise IOError('_gzFile.seek whence : %d Not managed yet' % whence)
##@brief Edf class to read Bzip2 file
#
try:
    import bz2
    class EdfBzip2File(EdfFile) :
        def __init__(self,filename,**keys) :
            self.__bzipFd = bz2.BZ2File(filename)
            EdfFile.__init__(self,self.__bzipFd,**keys)
except ImportError: pass

#EXEMPLE CODE:        
if __name__ == "__main__":
    if 1:
        import os
        a = numpy.zeros((5, 10))
        for i in range(5):
            for j in range(10):
                 a[i,j] = 10*i + j 
        edf = EdfFile("armando.edf")
        edf.WriteImage({},a)
        del edf #force to close the file
        inp = EdfFile("armando.edf")
        b = inp.GetData(0)
        out = EdfFile("armando2.edf")
        out.WriteImage({}, b)
        del out #force to close the file
        inp2 = EdfFile("armando2.edf")
        c = inp2.GetData(0)
        print "A SHAPE = ", a.shape
        print "B SHAPE = ", b.shape
        print "C SHAPE = ", c.shape
        for i in range(5):
            print "A", a[i,:]
            print "B", b[i,:]
            print "C", c[i,:]
            
        x = numpy.arange(100)
        x.shape = 5, 20
        for item in ["SignedByte", "UnsignedByte",
                     "SignedShort", "UnsignedShort", 
                     "SignedLong",  "UnsignedLong", 
                     "Signed64", "Unsigned64",
                     "FloatValue", "DoubleValue"]:
            fname = item + ".edf"
            if os.path.exists(fname):
                os.remove(fname)
            towrite = EdfFile(fname)
            towrite.WriteImage({}, x, DataType = item, Append=0)
        sys.exit(0)
    
    #Creates object based on file exe.edf
    exe=EdfFile("images/test_image.edf")
    x=EdfFile("images/test_getdata.edf")
    #Gets unsigned short data, storing in an signed long
    arr=exe.GetData(0,Pos=(100,200),Size=(200,400))
    x.WriteImage({},arr,0)

    arr=exe.GetData(0,Pos=(100,200))
    x.WriteImage({},arr)

    arr=exe.GetData(0,Size=(200,400))
    x.WriteImage({},arr)

    arr=exe.GetData(0)
    x.WriteImage({},arr)
    
    sys.exit()
        
    #Creates object based on file exe.edf
    exe=EdfFile("images/.edf")

    #Creates long array , filled with 0xFFFFFFFF(-1)
    la=numpy.zeros((100,100))
    la=la-1
    
    #Creates a short array, filled with 0xFFFF
    sa=numpy.zeros((100,100))
    sa=sa+0xFFFF
    sa=sa.astype("s")

    #Writes long array, initializing file (append=0)
    exe.WriteImage({},la,0,"")
    
    #Appends short array with new header items
    exe.WriteImage({'Name': 'Alexandre', 'Date': '16/07/2001'},sa)    

    #Appends short array, in Edf type unsigned
    exe.WriteImage({},sa,DataType="UnsignedShort")    

    #Appends short array, in Edf type unsigned
    exe.WriteImage({},sa,DataType="UnsignedLong")    

    #Appends long array as a double, considering unsigned
    exe.WriteImage({},la,DataType="DoubleValue",WriteAsUnsigened=1)

    #Gets unsigned short data, storing in an signed long
    ushort=exe.GetData(2,"SignedLong")

    #Makes an operation
    ushort=ushort-0x10

    #Saves Result as signed long
    exe.WriteImage({},ushort)

    #Saves in the original format (unsigned short)
    OldHeader=exe.GetStaticHeader(2)
    exe.WriteImage({},ushort,1,OldHeader["DataType"] )


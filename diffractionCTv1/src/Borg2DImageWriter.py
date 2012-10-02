#!/usr/bin/env python
# -*- Coding: UTF8 -*-
###########################################################################
# Written 2009-11-17 by Jerome Kieffer 
# Copyright (C) 2009 European Synchrotron Radiation Facility
#                       Grenoble, France
#
#    Principal authors: Jerome Kieffer  (jerome.kieffer@esrf.fr)
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
#############################################################################



"""
Borg2DImageWriter is a library implementing a Borg (more or less like a Singleton)   
"""
import os, threading, numpy
from    EDFactoryPluginStatic import  EDFactoryPluginStatic
from    EDVerbose             import  EDVerbose
# Use the EDF image header reader plugin for localising the EdfFile module
EDFactoryPluginStatic.loadModule("EDPluginEDFReadHeaderv1_0")
from    EdfFile                 import EdfFile

class Borg2DImageWriter():
    """
    Borg2DImageWriter is a library implementing a Borg (more or less like a Singleton) to write 2D images as EDF files
    keep in mind this is a borg and wil try to do some lock """

    __data_initialized = False
    __shared_state = {}
    def __init__(self):
        self.__dict__ = self.__shared_state
#       initialize the self.data and self.header only if they are not yet defined
        if  not Borg2DImageWriter.__data_initialized :
            Borg2DImageWriter.__data_initialized = True
            self.data = {}
            self.headers = {}
            self.edf = {}
            self.size = {}
            self.m_pySemaphore = threading.Semaphore()

    def synchronizeOn(self):
        """
        This method must be used in together with the method synchronizeOff().
        This method makes the code threadsafe till the method synchronizeOff
        is called.
        """
        self.m_pySemaphore.acquire()


    def synchronizeOff(self):
        """
        This method must be used in together with the method synchronizeOn().
        """
        self.m_pySemaphore.release()

    def newFile(self, filename="test", size=(0, 0), metadata={}):
        """this is a method to create a new empty file
        @param filename: name of the file to create, the size and the extension will be added.
        @type  filename: string
        @type size: 2-tuple of integers  
        @param size: the size of the image to create
        """
        if len(size) != 2 :
            EDVerbose.error("Error in the size of the size-tuple")
            raise Exception("Error in the size of the size-tuple")
        if size[0] < 0 :
            EDVerbose.error("Error in the X part of the size tuple")
            raise Exception("Error in the X part of the size tuple")
        if size[1] < 0 :
            EDVerbose.error("Error in the Y part of the size tuple")
            raise Exception("Error in the Y part of the size tuple")
        emptyNParray = numpy.zeros(size, dtype="float32")
        self.data[ filename ] = emptyNParray
        self.headers [ filename ] = metadata
        self.size [ filename ] = size
        fullFilename = "%sSize%ix%i.edf" % ((filename,) + size)
        if os.path.isfile(fullFilename):
            EDVerbose.warning("Warning, I am going to overwrite the file %s " % fullFilename)
            self.synchronizeOn()
            try:
                self.edf [ filename ] = EdfFile(fullFilename)
                self.data[ filename ] = self.edf[ filename ].GetData(0)
                self.headers [ filename ] = self.edf[ filename ].GetHeader(0)
            except Exception:
                EDVerbose.error("[ERROR] in reading file %s" % filename)
            self.synchronizeOff()
            if self.data[ filename ].shape != size :
                self.data[ filename ] = emptyNParray
                self.headers [ filename ] = metadata
        else:
            self.synchronizeOn()
            try:
                self.edf[ filename ] = EdfFile(fullFilename)
                self.edf[ filename ].WriteImage(self.headers [ filename ] , self.data [ filename ] , Append=0)
            except Exception:
                EDVerbose.error("[ERROR] in opening and creating file %s" % filename)
            self.synchronizeOff()

    def set(self, value=0, filename="test.edf", position=(0, 0)):
        """
        This is the set method that will first ensure that the data are available 
        #then set a lock on it and finally #No more 
        write the data 
        #before unlocking. #No more  
        @param: value value of the pixel to set
        @type value: probably float but can be any figure
        @param filename: name of the file to be processed
        @type filename: string
        @param position: the position of the pixel to modify 
        @type position: 2-tuple of integers  
        
        """
        if not isinstance(value, float):
            EDVerbose.error("ERROR The value %s is not a float" % value)
            raise Exception("ERROR The value %s is not a float" % value)
        if not (isinstance (filename, str) or isinstance (filename, unicode)):
            EDVerbose.error("ERROR The filename variable %s is not a string " % filename)
            raise Exception("ERROR The filename variable %s is not a string " % filename)
        if not isinstance (position, tuple):
            EDVerbose.error("ERROR The position variable %s is not a tuple " % position)
            raise Exception("ERROR The position variable %s is not a tuple " % position)
        if len(position) != 2 :
            EDVerbose.error("ERROR in the size of the position-tuple")
            raise Exception("ERROR in the size of the position-tuple")
        if position[0] < 0 :
            EDVerbose.error("ERROR in the X part of the position-tuple")
            raise Exception("ERROR in the X part of the position-tuple")
        if position[1] < 0 :
            EDVerbose.error("ERROR in the Y part of the position-tuple")
            raise Exception("ERROR in the Y part of the position-tuple")
        if not self.data.has_key(filename):
            EDVerbose.warning("ERROR, the destination image  %s is not in the list of images tracked : %s" % (filename, self.data.keys()))
            pystrDirname, pystrFilename = os.path.split(filename)
            fileInDir = []
            for onefile in os.listdir(pystrDirname):
                if  onefile.find("%sSize" % pystrFilename) == 0 :
                    if onefile[-4:].lower() == ".edf":
                        XxY = onefile.split("Size")[-1][:-4]
                        try:
                            size = tuple([ int(i) for i in tuple(XxY.split("x"))])
                        except Exception:
                            size = None
                        if size:
                            fileInDir.append(onefile)

            if len(fileInDir) > 1:
                EDVerbose.warning("ERROR, for %s, I found too many images corresponding to what you are looking for : %s" % (filename, fileInDir))
                raise Exception("ERROR, I found too many images corresponding to what you are looking for : %s" % (filename, fileInDir))
            elif  len(fileInDir) == 1:
                EDVerbose.warning("WARNING, As The file %s exists, I will try to read it. The expected size is %s" % (filename, size))
                self.size[ filename ] = size
                fullFilename = "%sSize%ix%i.edf" % ((filename,) + size)
                self.headers[ filename ] = {}
                self.data[ filename ] = numpy.zeros(size, dtype="float32")
                self.synchronizeOn()
                try:
                    self.edf[ filename ] = EdfFile(fullFilename)
                    self.headers[ filename ] = self.edf[ filename ].GetHeader(0)
                    self.data[ filename ] = self.edf[ filename ].GetData(0)
                except Exception:
                        EDVerbose.warning("ERROR in reading file %s: Reintializing it" % filename)
                        self.edf[ filename ] = EdfFile(fullFilename)
                        self.data[ filename ] = numpy.zeros(size , dtype="float32")
                        self.headers [ filename ] = {}
                self.synchronizeOff()

                if self.data[ filename ].shape != size:
                    self.data[ filename ] = numpy.zeros(size , dtype="float32")
                    self.headers[ filename ] = {}
            else:
                EDVerbose.error("ERROR, the destination image  %s is not in the list of images tracked : %s" % (filename, self.data.keys()))
                raise Exception("ERROR, the destination image  %s is not in the list of images tracked : %s" % (filename, self.data.keys()))


        if position[0] > self.data[ filename ].shape[0]:
            EDVerbose.error("ERROR in the X part of the position-tuple: too large %i > %i" % (position[0], npArray.shape[0]))
            raise Exception("ERROR in the X part of the position-tuple: too large %i > %i" % (position[0], npArray.shape[0]))
        if position[1] > self.data[ filename ].shape[1]:
            EDVerbose.error("ERROR in the Y part of the position-tuple: too large %i > %i" % (position[1], npArray.shape[1]))
            raise Exception("ERROR in the Y part of the position-tuple: too large %i > %i" % (position[1], npArray.shape[1]))
        self.data[ filename ][ position[0] , position[1] ] = value
        self.synchronizeOn()
        try:
            self.edf[ filename ].WriteImage(self.headers [ filename ], self.data[ filename ] , Append=0)
        except Exception:
            EDVerbose.error("ERROR in writing image %s at position %s" % (filename, position))
        self.synchronizeOff()

if __name__ == '__main__':
    print "This is just a test of the library"


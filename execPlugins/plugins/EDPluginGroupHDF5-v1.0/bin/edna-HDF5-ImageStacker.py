#!/usr/bin/env python
# -*- coding: utf8 -*-
#
#    Project: PROJECT
#             http://www.edna-site.org
#
#    File: "$Id$"
#
#    Copyright (C) European Synchrotron Radiation Facility, Grenoble, France
#
#    Principal author:       Jérôme Kieffer (Jerome.Kieffer@ESRF.eu)
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
__author__ = "Jerome Kieffer"
__contact__ = "Jerome.Kieffer@ESRF.eu"
__license__ = "GPLv3+"
__copyright__ = "European Synchrotron Radiation Facility, Grenoble, France"

import os, time, sys, threading, tempfile, string

# Append the EDNA kernel source directory to the python path
if not os.environ.has_key("EDNA_HOME"):
    pyStrProgramPath = os.path.abspath(sys.argv[0])
    pyLPath = pyStrProgramPath.split(os.sep)
    if len(pyLPath) > 5:
        pyStrEdnaHomePath = os.sep.join(pyLPath[:-5])
    else:
        print ("Problem in the EDNA_HOME path ..." + pyStrEdnaHomePath)
        sys.exit()

    os.environ["EDNA_HOME"] = pyStrEdnaHomePath


sys.path.append(os.path.join(os.environ["EDNA_HOME"], "kernel", "src"))
from EDParallelExecute import EDParallelExecute
from EDFactoryPluginStatic import EDFactoryPluginStatic
EDFactoryPluginStatic.loadModule("EDPluginHDF5StackImagesv10")
from EDPluginHDF5StackImagesv10 import EDPluginHDF5StackImagesv10
from XSDataHDF5v1_0 import XSDataInputHDF5StackImages, XSDataImageExt, XSDataInteger, XSDataFile, XSDataString
from EDUtilsArray import EDUtilsArray
import fabio
EDNAPluginName = "EDPluginHDF5StackImagesv10"

class MakeXML(object):
    def __init__(self, hdfFile=None):
        self.hdfFile = hdfFile
        self.index = 0
        self.dict = {}#key:index, value: filename
    def fileName2xml(self, filename):
        """Here we create the XML string to be passed to the EDNA plugin from the input filename
        This can / should be modified by the final user
        
        @param filename: full path of the input file
        @type filename: python string representing the path
        @rtype: XML string
        @return: python string  
        """

        basename = list(os.path.splitext(os.path.basename(filename))[0])
        basename.reverse()
        number = ""
        for i in basename:
            if i.isdigit():
                number = i + number
            else: break
        if self.hdfFile is None:
            self.hdfFile = os.path.splitext(filename)[0][:-len(number)] + ".h5"

        xsd = XSDataInputHDF5StackImages(index=[XSDataInteger(self.index)],
                                         HDF5File=XSDataFile(XSDataString(self.hdfFile)),
                                         internalHDF5Path=XSDataString("RawStack"),
                                         inputImageFile=[XSDataImageExt(path=XSDataString(filename))]
                                         )
#                                         inputArray=[EDUtilsArray.arrayToXSData(fabio.open(filename).data)])

        self.dict[self.index] = filename
        self.index += 1
        return xsd.marshal()

    def errBack(self, strXMLin):
        """
        This is an example of XMLerr function ... it prints only the name of the file created
        @param srXMLin: The XML string used to launch the job
        @type strXMLin: python string with the input XML
        @rtype: None
        @return: None     
        """
        xsd = XSDataInputHDF5StackImages.parseString(strXMLin)
        print "Error in the processing of : %s" % (self.dict[xsd.index[0].value])



if __name__ == '__main__':
    paths = []
    mode = "OffLine"
    newerOnly = True
    debug = False
    iNbCPU = None
    hdf5 = None
    for i in sys.argv[1:]:
        if i.lower().find("-online") in [0, 1]:
            mode = "dirwatch"
        elif i.lower().find("-all") in [0, 1]:
            newerOnly = False
        elif i.lower().find("-debug") in [0, 1]:
            debug = True
        elif i.lower().find("-ncpu") in [0, 1]:
            iNbCPU = int(i.split("=", 1)[1])
        elif i.lower().find("-h") in [0, 1]:
            hdf5 = i.split("=", 1)[1]
        elif os.path.exists(i):
            paths.append(os.path.abspath(i))
    print hdf5
    mkXml = MakeXML(hdf5)
    if len(paths) == 0:
        if mode == "OffLine":
            print "This is the HDF5 3D image stacker application of EDNA, \nplease give a path to process offline or the option:\n\
            --online to process online incoming data in the given directory.\n\
            --all to process all existing files (unless they will be excluded)\n\
            --debug to turn on debugging mod in EDNA"

            sys.exit()
        else:
            paths = [os.getcwd()]
    edna = EDParallelExecute(EDNAPluginName, mkXml.fileName2xml, _functXMLerr=mkXml.errBack, _bVerbose=True, _bDebug=debug, _iNbThreads=iNbCPU)
    edna.runEDNA(paths, mode , newerOnly)
    print "Back in main"
    EDPluginHDF5StackImagesv10.closeAll()

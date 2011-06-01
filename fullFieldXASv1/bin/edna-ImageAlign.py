#!/usr/bin/env python
# -*- coding: utf8 -*-
#
#    Project: PROJECT Full Field XAS
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
    if len(pyLPath) > 3:
        pyStrEdnaHomePath = os.sep.join(pyLPath[:-3])
    else:
        print ("Problem in the EDNA_HOME path ..." + pyStrEdnaHomePath)
        sys.exit()

    os.environ["EDNA_HOME"] = pyStrEdnaHomePath


sys.path.append(os.path.join(os.environ["EDNA_HOME"], "kernel", "src"))
from EDParallelExecute import EDParallelExecute
from EDVerbose import EDVerbose
from EDFactoryPluginStatic import EDFactoryPluginStatic
#EDFactoryPluginStatic.loadModule('EDPluginHDF5StackImagesv10')
#from EDPluginHDF5StackImagesv10 import EDPluginHDF5StackImagesv10
EDFactoryPluginStatic.loadModule('EDPluginControlAlignStackv1_0')
from EDPluginControlAlignStackv1_0 import EDPluginControlAlignStackv1_0

EDNAPluginName = "EDPluginControlAlignStackv1_0"

def fileName2xml(filename):
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
    hdf5File = os.path.splitext(filename)[0][:-len(number)] + "alignVsRef+background+smooth+.h5"
    xml = "<XSDataInput>\
    <HDF5File><path><value>%s</value></path></HDF5File>\
    <internalHDF5Path><value>AlignedStack</value></internalHDF5Path>\
    <image>\
        <path><value>%s</value></path>\
    </image>\
    <index><value>%s</value></index>\
    <alwaysMOvsRef><value>1</value></alwaysMOvsRef>\
    <multiFiles><value>0</value></multiFiles>\
    <frameReference><value>0</value></frameReference>\
    <backgroundSubtractionMO><value>1</value></backgroundSubtractionMO>\
    <smoothBordersMO><value>100</value></smoothBordersMO>\
    </XSDataInput>" % (hdf5File, filename, number)
#    print filename + " should be on position " + number
#<cropBorders><value>512</value></cropBorders>\
#    <backgroundSubtractionMO><value>1</value></backgroundSubtractionMO>\
#    <smoothBordersMO><value>50</value></smoothBordersMO>\

    return xml

def XMLerr(strXMLin):
    """
    This is an example of XMLerr function ... it prints only the name of the file created
    @param srXMLin: The XML string used to launch the job
    @type strXMLin: python string with the input XML
    @rtype: None
    @return: None     
    """
    print "Error in the processing of :"
    print strXMLin
    return None


if __name__ == '__main__':
    paths = []
    mode = "OffLine"
    newerOnly = True
    debug = False
    iNbCPU = None
    for i in sys.argv[1:]:
        if i.lower().find("-online") in [0, 1]:
            mode = "dirwatch"
        elif i.lower().find("-all") in [0, 1]:
            newerOnly = False
        elif i.lower().find("-debug") in [0, 1]:
            debug = True
        elif i.lower().find("-ncpu") in [0, 1]:
            iNbCPU = int(i.split("=", 1)[1])
        elif os.path.exists(i):
            paths.append(os.path.abspath(i))

    if len(paths) == 0:
        if mode == "OffLine":
            print "This is the HDF5 3D image stacker application of EDNA with image alignment, \nplease give a path to process offline or the option:\n\
            --online to process online incoming data in the given directory.\n\
            --all to process all existing files (unless they will be excluded)\n\
            --debug to turn on debugging mod in EDNA"

            sys.exit()
        else:
            paths = [os.getcwd()]
    edna = EDParallelExecute(EDNAPluginName, fileName2xml, _functXMLerr=XMLerr, _bVerbose=True, _bDebug=debug, _iNbThreads=iNbCPU)
    edna.runEDNA(paths, mode , newerOnly)
    EDVerbose.screen("Back in main")
    EDPluginControlAlignStackv1_0.showData()
#    EDPluginHDF5StackImagesv10.closeAll()
